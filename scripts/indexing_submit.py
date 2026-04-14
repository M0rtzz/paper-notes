#!/usr/bin/env python3
"""
搜索引擎索引提交脚本：Google Indexing API + Bing IndexNow。

用法:
  # Google + Bing 同时提交
  python src/google_indexing_submit.py --credentials sa.json --bing-key YOUR_KEY

  # 仅 Bing IndexNow（无需额外认证，无配额限制）
  python src/google_indexing_submit.py --bing-only --bing-key YOUR_KEY

  # 仅 Google
  python src/google_indexing_submit.py --credentials sa.json --google-only

  # 仅提交最近变更的文件
  python src/google_indexing_submit.py --credentials sa.json --bing-key YOUR_KEY --changed-only

Google 前置条件:
  1. Google Cloud 项目启用 Indexing API
  2. 创建 Service Account 并下载 JSON 密钥
  3. 在 Google Search Console 中将 Service Account 邮箱添加为 Owner
  4. pip install google-auth google-auth-httplib2 google-api-python-client

Bing IndexNow 前置条件:
  1. 生成一个 key（任意 UUID 即可）
  2. 在站点根目录放置 {key}.txt 文件（内容为 key 本身）
  3. 无需额外依赖
"""

import argparse
import json
import os
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
SITE_URL = "https://zhaoyang97.github.io/Paper-Notes/"
HOST = "zhaoyang97.github.io"
DAILY_QUOTA = 200
INDEXNOW_BATCH_SIZE = 10000  # IndexNow 单次最大 10,000 条
PROGRESS_FILE = "logs/indexing_progress.json"


def parse_args():
    p = argparse.ArgumentParser(description="Google Indexing API + Bing IndexNow 批量提交")
    p.add_argument("--credentials", default=None,
                   help="Google Service Account JSON 密钥文件路径")
    p.add_argument("--bing-key", default=None,
                   help="Bing IndexNow key")
    p.add_argument("--google-only", action="store_true",
                   help="仅提交 Google")
    p.add_argument("--bing-only", action="store_true",
                   help="仅提交 Bing IndexNow")
    p.add_argument("--sitemap", default=None,
                   help="sitemap.xml 路径（默认从线上获取）")
    p.add_argument("--changed-only", action="store_true",
                   help="仅提交 git 最近变更的文件")
    p.add_argument("--dry-run", action="store_true",
                   help="仅打印要提交的 URL，不实际提交")
    p.add_argument("--limit", type=int, default=DAILY_QUOTA,
                   help=f"Google 单次最大提交数（默认 {DAILY_QUOTA}）")
    p.add_argument("--action", choices=["URL_UPDATED", "URL_DELETED"],
                   default="URL_UPDATED",
                   help="提交动作类型（默认 URL_UPDATED）")
    return p.parse_args()


def load_progress() -> dict:
    """加载已提交的进度记录"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"submitted": {}, "total_submitted": 0}


def save_progress(progress: dict):
    """保存进度"""
    os.makedirs(os.path.dirname(PROGRESS_FILE), exist_ok=True)
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def get_urls_from_sitemap(sitemap_path: str) -> list[str]:
    """从 sitemap 或 sitemap index 解析所有 URL"""
    urls = []
    tree = ET.parse(sitemap_path)
    root = tree.getroot()

    # 检查是否为 sitemap index
    sitemaps = root.findall(f"{{{NS}}}sitemap")
    if sitemaps:
        # sitemap index: 递归解析每个子 sitemap
        site_dir = os.path.dirname(sitemap_path)
        for sm in sitemaps:
            loc = sm.find(f"{{{NS}}}loc")
            if loc is not None:
                # 从 URL 提取文件名
                filename = loc.text.split("/")[-1]
                sub_path = os.path.join(site_dir, filename)
                if os.path.exists(sub_path):
                    urls.extend(get_urls_from_sitemap(sub_path))
    else:
        # 普通 sitemap
        for url_elem in root.findall(f"{{{NS}}}url"):
            loc = url_elem.find(f"{{{NS}}}loc")
            if loc is not None:
                urls.append(loc.text)

    return urls


def get_urls_from_remote_sitemap(sitemap_url: str) -> list[str]:
    """从远端 sitemap 获取 URL 列表"""
    import urllib.request
    urls = []
    try:
        with urllib.request.urlopen(sitemap_url, timeout=30) as resp:
            content = resp.read().decode("utf-8")
        root = ET.fromstring(content)

        sitemaps = root.findall(f"{{{NS}}}sitemap")
        if sitemaps:
            for sm in sitemaps:
                loc = sm.find(f"{{{NS}}}loc")
                if loc is not None:
                    urls.extend(get_urls_from_remote_sitemap(loc.text))
        else:
            for url_elem in root.findall(f"{{{NS}}}url"):
                loc = url_elem.find(f"{{{NS}}}loc")
                if loc is not None:
                    urls.append(loc.text)
    except Exception as e:
        print(f"❌ 获取远端 sitemap 失败: {e}")
    return urls


def get_changed_urls() -> list[str]:
    """从 git diff 获取最近变更的论文页 URL"""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1", "HEAD",
             "--", "paper_notes/docs/"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            print(f"⚠️ git diff 失败: {result.stderr}")
            return []

        urls = []
        for line in result.stdout.strip().split("\n"):
            if not line or not line.endswith(".md"):
                continue
            # paper_notes/docs/ICLR2026/image_generation/xxx.md -> URL
            rel = line.replace("paper_notes/docs/", "")
            rel = rel.replace(".md", "/")
            if rel.endswith("index/"):
                rel = rel.replace("index/", "")
            url = SITE_URL + rel
            urls.append(url)

        return urls
    except Exception as e:
        print(f"⚠️ 获取变更文件失败: {e}")
        return []


def filter_paper_urls(urls: list[str]) -> list[str]:
    """过滤出论文笔记页（排除 index/TODO 等）"""
    filtered = []
    for url in urls:
        path = url.replace(SITE_URL, "")
        # 排除首页、TODO 页、纯 index 页
        if not path or path == "/":
            continue
        parts = path.strip("/").split("/")
        if len(parts) < 3:
            continue  # 至少需要 会议/领域/论文
        if parts[-1] in ("TODO", "index"):
            continue
        filtered.append(url)
    return filtered


def submit_urls(urls: list[str], credentials_path: str, action: str,
                dry_run: bool = False) -> tuple[int, int]:
    """
    使用 Google Indexing API 提交 URL。
    返回 (成功数, 失败数)。
    """
    if dry_run:
        for url in urls:
            print(f"  [DRY-RUN] Google {action}: {url}")
        return len(urls), 0

    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
    except ImportError:
        print("❌ 缺少依赖，请运行:")
        print("   pip install google-auth google-auth-httplib2 google-api-python-client")
        sys.exit(1)

    SCOPES = ["https://www.googleapis.com/auth/indexing"]
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path, scopes=SCOPES
    )
    service = build("indexing", "v3", credentials=credentials)

    success = 0
    fail = 0
    progress = load_progress()

    for i, url in enumerate(urls):
        try:
            body = {"url": url, "type": action}
            service.urlNotifications().publish(body=body).execute()
            success += 1
            progress["submitted"][url] = {
                "time": datetime.now().isoformat(),
                "action": action,
                "engine": "google",
            }
            progress["total_submitted"] = len(progress["submitted"])

            if (i + 1) % 10 == 0:
                print(f"  进度: {i+1}/{len(urls)} (成功: {success}, 失败: {fail})")
                save_progress(progress)

            # 遵守速率限制
            time.sleep(0.5)

        except Exception as e:
            fail += 1
            error_msg = str(e)
            if "429" in error_msg or "quota" in error_msg.lower():
                print(f"  ⚠️ 达到 API 配额限制，已提交 {success} 条")
                break
            print(f"  ❌ 提交失败 [{url}]: {error_msg}")

    save_progress(progress)
    return success, fail


def submit_urls_indexnow(urls: list[str], key: str,
                         dry_run: bool = False) -> tuple[int, int]:
    """
    使用 Bing IndexNow API 批量提交 URL。
    IndexNow 支持单次最多 10,000 条，无每日配额限制。
    返回 (成功数, 失败数)。
    """
    import urllib.request

    if dry_run:
        for url in urls[:5]:
            print(f"  [DRY-RUN] IndexNow: {url}")
        if len(urls) > 5:
            print(f"  [DRY-RUN] ... 共 {len(urls)} 条")
        return len(urls), 0

    success = 0
    fail = 0

    # 分批提交（每批最多 10,000 条）
    for batch_start in range(0, len(urls), INDEXNOW_BATCH_SIZE):
        batch = urls[batch_start:batch_start + INDEXNOW_BATCH_SIZE]
        payload = json.dumps({
            "host": HOST,
            "key": key,
            "keyLocation": f"https://{HOST}/Paper-Notes/{key}.txt",
            "urlList": batch,
        }).encode("utf-8")

        req = urllib.request.Request(
            "https://api.indexnow.org/indexnow",
            data=payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                status = resp.status
            if status in (200, 202):
                success += len(batch)
                print(f"  ✅ IndexNow 批次提交成功: {len(batch)} 条 (HTTP {status})")
            else:
                fail += len(batch)
                print(f"  ⚠️ IndexNow 返回 HTTP {status}")
        except Exception as e:
            fail += len(batch)
            print(f"  ❌ IndexNow 提交失败: {e}")

    return success, fail


def main():
    args = parse_args()

    # 确定提交引擎
    do_google = not args.bing_only and args.credentials
    do_bing = not args.google_only and args.bing_key

    if not do_google and not do_bing:
        print("❌ 至少需要指定 --credentials (Google) 或 --bing-key (Bing)")
        sys.exit(1)

    engines = []
    if do_google:
        engines.append("Google")
    if do_bing:
        engines.append("Bing IndexNow")
    print(f"🔧 提交引擎: {' + '.join(engines)}")

    # 1. 获取 URL 列表
    if args.changed_only:
        print("📋 获取 git 变更文件...")
        all_urls = get_changed_urls()
        print(f"   变更页面: {len(all_urls)}")
    elif args.sitemap:
        print(f"📋 解析本地 sitemap: {args.sitemap}")
        all_urls = get_urls_from_sitemap(args.sitemap)
        print(f"   总 URL 数: {len(all_urls)}")
    else:
        print(f"📋 获取远端 sitemap: {SITE_URL}sitemap.xml")
        all_urls = get_urls_from_remote_sitemap(f"{SITE_URL}sitemap.xml")
        print(f"   总 URL 数: {len(all_urls)}")

    # 2. 过滤论文页
    paper_urls = filter_paper_urls(all_urls)
    print(f"   论文页: {len(paper_urls)}")

    if not paper_urls:
        print("⚠️ 没有找到需要提交的论文页")
        return

    # === Bing IndexNow ===
    if do_bing:
        print(f"\n{'='*50}")
        print(f"📤 Bing IndexNow: 提交 {len(paper_urls)} 条 (无配额限制)")
        if args.dry_run:
            print("⚠️ DRY-RUN 模式\n")
        bing_ok, bing_fail = submit_urls_indexnow(
            paper_urls, args.bing_key, args.dry_run
        )
        print(f"   Bing 结果: 成功 {bing_ok}, 失败 {bing_fail}")

    # === Google Indexing API ===
    if do_google:
        # Google 有配额，需要断点续传
        progress = load_progress()
        already_submitted = set(progress.get("submitted", {}).keys())
        pending = [u for u in paper_urls if u not in already_submitted]
        print(f"\n{'='*50}")
        print(f"📤 Google Indexing API:")
        print(f"   待提交: {len(pending)} (已提交: {len(already_submitted)})")

        if not pending:
            print("   ✅ Google: 所有论文页已提交！")
        else:
            batch = pending[:args.limit]
            print(f"   本次提交: {len(batch)} 条 (限额: {args.limit})")
            if args.dry_run:
                print("   ⚠️ DRY-RUN 模式\n")

            google_ok, google_fail = submit_urls(
                batch, args.credentials, args.action, args.dry_run
            )
            print(f"   Google 结果: 成功 {google_ok}, 失败 {google_fail}")
            remaining = len(pending) - len(batch)
            if remaining > 0:
                days = remaining // args.limit + 1
                print(f"   剩余: {remaining} 条, 预计 {days} 天完成")


if __name__ == "__main__":
    main()
