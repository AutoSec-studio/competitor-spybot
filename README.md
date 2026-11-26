# CompetitorPulse Spybot 🕵️⚡

> **Stealth E-Commerce Competitor Price Radar & Stockout Intelligence Engine**
> <p align="left">
  <a href="https://github.com/AutoSec-studio/competitor-spybot"><img src="https://img.shields.io/badge/python-3.10+-3776AB.svg?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square" alt="MIT License"></a>
  <a href="https://github.com/AutoSec-studio/competitor-spybot"><img src="https://img.shields.io/badge/tests-8%20passed-brightgreen?style=flat-square&logo=pytest" alt="Tests"></a>
  <a href="https://github.com/AutoSec-studio/competitor-spybot"><img src="https://img.shields.io/badge/Stealth_Radar-Zero_Proxy_Fees-00F59B?style=flat-square" alt="Stealth"></a>
  <a href="https://t.me/autosec_studio"><img src="https://img.shields.io/badge/Telegram-@autosec__studio-229ED9?style=flat-square&logo=telegram&logoColor=white" alt="Telegram"></a>
  <a href="https://whop.com/autosec/"><img src="https://img.shields.io/badge/Whop_Store-Get_Pro_$10-FF5C00?style=flat-square&logo=whop&logoColor=white" alt="Whop"></a>
  <a href="https://payhip.com/"><img src="https://img.shields.io/badge/Payhip-Get_Pro_$10-00D2FF?style=flat-square" alt="Payhip"></a>
</p>

A self-hosted, autonomous competitor monitoring system for Shopify, WooCommerce, and modern DTC brands. Detect competitor price drops, flash discounts, inventory stockouts, and catalog updates 24/7 with instant Telegram, Slack, and Webhook alerts.

---

## ⚡ The Business Problem It Solves

* **Silent Competitor Undercutting:** Competitors launch flash sales or price cuts on key hero products. If you take 48 hours to notice, your ad budget burns while their store captures the traffic.
* **Capitalizing on Competitor Stockouts:** When your rival runs out of stock, they cannot fulfill customer demand. CompetitorPulse Spybot notifies you instantly so you can increase your ad budget and capture their stranded buyers.
* **Zero Monthly Subscriptions:** Avoid expensive SaaS pricing ($49 - $199/month). Own your monitoring engine forever.

---

## 🚀 Key Features

* 🕵️ **Stealth Crawling Architecture:** User-Agent rotation and jitter delay prevent bot blocks.
* 🛍️ **Multi-Platform Support:** Native Shopify JSON API parsing, Schema.org microdata, OpenGraph tags, and custom CSS selectors.
* 📉 **Intelligent Variation Triggers:** Configurable percentage thresholds for price drops (`alert_on_price_drop_pct`) and price increases.
* 📦 **Stockout & Restock Detection:** Instant alerts when competitor inventory empties or restocks.
* 📱 **Actionable Telegram Cards:** Rich formatted HTML alerts with percentage change badges and direct `[ View Competitor Product ]` buttons.
* 💾 **Persistent SQLite WAL Engine:** Zero data loss, historical price tracking, and intelligent cooldown deduplication.
* 🐳 **Docker-Ready:** Deploy in seconds via `docker compose up -d` or standard Python 3.12.

---

## 🛠️ Quickstart (3 Minutes)

### Option A: Local Python
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run diagnostics & setup
python scripts/verify_setup.py

# 3. Configure your targets in config/config.yaml and tokens in .env
# 4. Launch the spybot
python main.py
```

### Option B: Docker Compose
```bash
docker compose up -d --build
```

---

## ⚙️ Configuration Example (`config/config.yaml`)

```yaml
targets:
  - id: "competitor_hero"
    name: "Competitor Headphones"
    url: "https://competitor-store.com/products/wireless-headphones"
    mode: "shopify_json"
    check_interval_seconds: 300
    triggers:
      alert_on_price_drop_pct: 5.0
      alert_on_price_increase_pct: 10.0
      alert_on_stockout: true
      alert_on_back_in_stock: true
```

---

Developed with ❤️ by **AutoSec Studio** — Autonomous E-Commerce & Business Intelligence Engines.
