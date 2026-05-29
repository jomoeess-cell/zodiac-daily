#!/usr/bin/env python3
"""
Gemini Horoscope Daily Scraper - ELLE Astrology (Production Ready)
自動爬取雙子座今日運勢並推送到 Telegram
"""

import urllib.request
import json
import re
from datetime import datetime
import time
import os

TELEGRAM_BOT_TOKEN = "8770323806:AAF7okArDK30Jj30CD8PsTXQDqm0ftIX_jI"
TELEGRAM_CHAT_ID = "8798582756"
LOG_FILE = "/tmp/zodiac-daily.log"

def log(message):
    """Log to both console and file"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def fetch_url(url):
    """Fetch URL with proper headers"""
    log(f"🔍 正在抓取：{url}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8'
    }
    
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode('utf-8')
            return html
    except Exception as e:
        log(f"❌ 抓取失敗：{e}")
        return None

def parse_horoscope(html):
    """Parse horoscope data from ELLE page"""
    if not html:
        return None
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Extract description using proper regex escaping
    desc_match = re.search(r'<meta[^>]+name=["\']sailthru\.excerpt["\'][^>]+content=["\']([^"\'>]+)', html, re.IGNORECASE)
    
    if desc_match:
        description = desc_match.group(1).strip()
    else:
        log("⚠️ 未找到描述，使用標題代替")
        title_match = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\'>]+)', html, re.IGNORECASE)
        description = title_match.group(1).strip() if title_match else "雙子座運勢"
    
    # Extract date from meta tags
    date_match = re.search(r'<meta[^>]+property=["\']article:published_time["\'][^>]+content=["\']([^"\'>]+)', html, re.IGNORECASE)
    publish_date = date_match.group(1).strip() if date_match else today
    
    # Get site name
    site_match = re.search(r'<meta[^>]+name=["\']generator["\'][^>]+content=["\']([^"\'>]+)', html, re.IGNORECASE)
    site_name = site_match.group(1).strip() if site_match else "ELLE 星座"
    
    # Get excerpt link if available
    link_match = re.search(r'<meta[^>]+property=["\']article:url["\'][^>]+content=["\']([^"\'>]+)', html, re.IGNORECASE)
    excerpt_link = link_match.group(1).strip() if link_match else "#"
    
    # Build final message
    message = f"""**🌟 {site_name} - 雙子座運勢 ({today})**

> **發布時間**: {publish_date}
> **文章連結**: [{description}]({excerpt_link})
>
---
*來源：https://share.google/u8zh8N8LAMDHdwSuO*
"""
    return message

def send_telegram(message):
    """Send message to Telegram"""
    if not message or not TELEGRAM_BOT_TOKEN:
        log("❌ 無有效訊息或 Token")
        return
    
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        
        payload = json.dumps({
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown',
            'disable_notification': False
        }).encode('utf-8')
        
        headers = {'Content-Type': 'application/json'}
        req = urllib.request.Request(url, data=payload, headers=headers, method='POST')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode('utf-8'))
        
        if result.get('ok'):
            log(f"✅ 推送成功！Message ID: {result['result']['message_id']}")
            return True
        else:
            log(f"❌ API 返回：{result}")
            return False
            
    except Exception as e:
        log(f"❌ 推送失敗：{e}")
        return False

if __name__ == "__main__":
    log("=" * 60)
    log("🔮 Gemini Horoscope Daily Scraper - 執行中")
    log("=" * 60)
    
    # Fetch URL from environment or use default
    url = os.environ.get('TELEGRAM_BOT_URL', "https://share.google/u8zh8N8LAMDHdwSuO")
    
    html = fetch_url(url)
    if not html:
        log("❌ 無法抓取頁面，終止")
        exit(1)
    
    message = parse_horoscope(html)
    if not message:
        log("❌ 解析失敗，終止")
        exit(1)
    
    log(f"\n📝 待推送內容:")
    log("-" * 40)
    print(message)
    log("-" * 40)
    
    success = send_telegram(message)
    if success:
        log("\n✅ Horoscope scraping completed successfully!")
    else:
        log("\n❌ Horoscope scraping failed to push to Telegram")
