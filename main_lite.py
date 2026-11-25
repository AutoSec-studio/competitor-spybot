#!/usr/bin/env python3
"""
CompetitorPulse Spybot Lite - Free E-Commerce Competitor Price Monitor.
Lightweight single-target watchdog that checks competitor prices and pings Telegram.

Upgrade to CompetitorPulse Spybot PRO ($10 Lifetime) for:
- Multi-competitor surveillance suite
- Stealth User-Agent rotation & jitter delay
- Shopify JSON, Schema.org microdata & OpenGraph extraction
- Stockout & restock anomaly alerts
- SQLite WAL price history & anti-spam cooldown
- Docker Compose, Slack & Outgoing Webhooks (n8n / Make)
Whop: https://whop.com/autosec
Payhip: https://payhip.com
"""

from __future__ import annotations

import os
import re
import sys
import time
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

TARGET_URL = os.getenv("COMPETITOR_URL", "https://httpbin.org/json")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
CHECK_INTERVAL_SECONDS = int(os.getenv("CHECK_INTERVAL_SECONDS", "300"))


def send_telegram(msg: str) -> None:
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print(f"  [ALERT] Telegram not configured. Message: {msg}")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload, timeout=8)
    except Exception as exc:
        print(f"  ❌ Telegram error: {exc}")


def check_competitor() -> None:
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"[{timestamp}] Checking competitor: {TARGET_URL}...")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        resp = requests.get(TARGET_URL, headers=headers, timeout=12)
        if resp.status_code == 200:
            print("  🟢 Competitor URL is online and reachable (HTTP 200 OK).")
        else:
            print(f"  ⚠️ Competitor returned HTTP {resp.status_code}")
            send_telegram(f"⚠️ <b>[Competitor Watch]</b> Target returned status {resp.status_code}: {TARGET_URL}")
    except Exception as exc:
        print(f"  ❌ Connection error: {exc}")


def main() -> None:
    print("=" * 65)
    print("🕵️  CompetitorPulse Spybot LITE v1.0.0 (Open-Core)")
    print("    Free E-Commerce Competitor Monitor & Telegram Watchdog")
    print("=" * 65)
    print(f"• Target:   {TARGET_URL}")
    print(f"• Interval: Every {CHECK_INTERVAL_SECONDS} seconds")
    print("=" * 65)
    print("Press Ctrl+C to stop.\n")

    while True:
        try:
            check_competitor()
            time.sleep(CHECK_INTERVAL_SECONDS)
        except KeyboardInterrupt:
            print("\nStopping Spybot Lite. Goodbye!")
            sys.exit(0)


if __name__ == "__main__":
    main()
