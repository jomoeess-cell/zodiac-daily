---
name: zodiac-daily
description: Auto-crawl Gemini (雙子座) daily horoscope at 06:00, compile into formatted article and send to Telegram.
version: 3.0.0
author: Hermes Agent Official
license: MIT
platforms: [linux, macos, windows, wsl]
metadata:
  hermes:
    tags: [Zodiac, Horoscope, Daily-Horoscope, Gemini, ELLE-Astrology]
    category: social-media
prerequisites:
  - python3
  - requests or urllib (stdlib)
  - json library
user_preferences:
  language: zh-TW (繁體中文優先)
  style: concise_direct (簡潔直接，避免冗長解釋)
  output_format: structured_cronjob_response
---

# Zodiac Daily Horoscope Skill (雙子座運勢自動抓取) v3.0

Automated daily horoscope delivery for Gemini (雙子座). Crawls ELLE astrology at 06:00 AM, extracts today's forecast data, and delivers formatted articles to Telegram.

## User Preferences ⚡

| 項目 | 偏好設定 |
|------|---------|
| **語言** | 🇹🇼 繁體中文優先（除非使用者指定其他語言） |
| **風格** | ✅ 簡潔直接，不需冗長解釋或重複格式步驟 |
| **輸出格式** | 📊 Cronjob 結構化運勢分析輸出 |

---

## Features

- ✅ **Auto-crawling**: Fetches Gemini horoscope from ELLE at 06:00 daily
- ✅ **Structured Extraction**: Parses luck numbers, colors, directions, timing
- ✅ **Formatted Articles**: Clean Markdown formatting with emojis
- ✅ **Telegram Delivery**: Direct send to user channel (with Bot Token)
- ✅ **Fallback Patterns**: Handles redirect chains gracefully
- ✅ **WSL Compatible**: Uses standard library only

## Installation

### Via Hermes Skills (Recommended)

```bash
# Skill location: ~/.hermes/skills/social-media/zodiac-daily/
cd ~/.hermes/skills/social-media/zodiac-daily/
```

### Script File

```bash
~/.hermes/skills/social-media/zodiac-daily/scripts/gemini-horoscope.py
```

## Usage

### Run Manually

```bash
python3 ~/.hermes/skills/social-media/zodiac-daily/scripts/gemini-horoscope.py
```

Or run from script directory:

```bash
cd ~/.hermes/skills/social-media/zodiac-daily/scripts/
python3 gemini-horoscope.py
```

### Cron Job Setup (Recommended for Automation)

**Option 1: Using system crontab**

Create/edit crontab entry:

```bash
# Add to crontab (~/.crontab or /etc/crontab)
# Hourly format: minute hour day month weekday command
0 6 * * * /usr/bin/python3 ~/.hermes/skills/social-media/zodiac-daily/scripts/gemini-horoscope.py >> /tmp/zodiac-daily.log 2>&1
```

Set up crontab:

```bash
crontab ~/.crontab
```

**Option 2: Create dedicated crontab file**

```bash
echo "0 6 * * * /usr/bin/python3 ~/.hermes/skills/social-media/zodiac-daily/scripts/gemini-horoscope.py >> /tmp/zodiac-daily.log 2>&1" > ~/.crontab.d/daily-gemini-horoscope
cat ~/.crontab.d/daily-gemini-horoscope
```

### Hermes Cronjob Tool (If Available)

```bash
cronjob create \
  --name "daily-gemini-horoscope" \
  --schedule "0 6 * * *" \
  --repeat 365 \
  --skill "zodiac-daily" \
  --deliver telegram:8798582756
```

Run one-time:

```bash
cronjob run --job-id daily-gemini-horoscope
```

## Configuration

### Required: Telegram Bot Token

To send horoscopes to Telegram, you need to configure a Bot Token:

1. Open Telegram and search for `@BotFather`
2. Create a new bot with `/newbot` command
3. Copy the token provided (looks like: `1234567890:AAH...)
4. Edit the script:

```bash
nano ~/.hermes/skills/social-media/zodiac-daily/scripts/gemini-horoscope.py
```

Replace this line:

```python
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
```

With your actual bot token:

```python
TELEGRAM_BOT_TOKEN = "1234567890:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Important: Channel Setup

After getting the bot token:

1. Send a message to your Telegram channel/group
2. Your bot must be added as an administrator with permission to send messages
3. Use the channel's username or ID in `TELEGRAM_CHAT_ID`

Example for sending to a group by invite link (not recommended for automation):

```python
TELEGRAM_CHAT_ID = "8798582756"  # Replace with actual chat ID or username
```

## API Endpoint

**Target URL**: `https://www.elle.com/tw/starsigns/today/a21025248/gemini-today/`

The script extracts data from the `sailthru.excerpt` meta tag in the page HTML.

## Extraction Fields

The following fields are extracted from ELLE's horoscope:

```python
{
    "date": str,                    # Today's date (YYYY-MM-DD)
    "luck_number": int,             # 幸運數字 (1-5 range after normalization)
    "luck_color": str,              # 幸運顏色
    "luck_direction": str,          # 開運方位
    "luck_time": str,               # 今日吉時
    "luck_sign": str,               # 幸運星座
    "description": str              # Overall forecast text
}
```

## Message Template

The generated article follows this format:

```markdown
## 📊 雙子座今日運勢（{date}）

### ✨ 基本資訊
- **星座**：雙子座 (05/21 ~ 06/21)
- **幸運數字**：{luck_number}⭐️
- **幸運顏色**：{luck_color}
- **開運方位**：{luck_direction}
- **今日吉時**：{luck_time}
- **幸運星座**：{luck_sign}

---

### 📈 整體運勢

> 💡 {description}

---

*資料來源：ELLE 星座運勢 | {url}*
```

## Example Output (Latest)

When executed, the script produces output like:

```bash
[2026-05-26 06:22:37] ============================================================
[2026-05-26 06:22:37] 🎯 開始執行雙子座運勢抓取
[2026-05-26 06:22:37] ============================================================
[2026-05-26 06:22:37] 🔍 正在抓取：https://www.elle.com/tw/starsigns/today/a21025248/gemini-today/
[2026-05-26 06:22:37] ✅ 找到 excerpt
[2026-05-26 06:22:37] ✅ 解析結果:
[2026-05-26 06:22:37]    ✓ luck_number: 6
[2026-05-26 06:22:37]    ✓ luck_color: 淺海藍
[2026-05-26 06:22:37]    ✓ luck_direction: 西北方向
[2026-05-26 06:22:37]    ✓ luck_time: 7:00-8:00am
[2026-05-26 06:22:37]    ✓ luck_sign: 天蠍座
[2026-05-26 06:22:37]    ✓ description: 情緒較低，生活的挫折讓你心灰意懶。
[2026-05-26 06:22:37] ✅ 文章生成完成
[2026-05-26 06:22:37] 📝 ## 📊 雙子座今日運勢（2026-05-26）
...
[2026-05-26 06:22:37] ✅ 任務完成！
```

## Fallback Patterns

### Pattern 1: Browser Exit Recovery (WSL)

The script uses `urllib` from Python standard library, so it works on WSL without needing Chrome/Python browser integration.

### Pattern 2: Redirect Chain Handling

The script handles HTTP redirects automatically with proper User-Agent headers.

### Pattern 3: Zero-Dependency Mode

No external dependencies required - uses only Python standard library (`urllib`, `json`, `re`, `datetime`).

### 🆕 Pattern 4: Telegram API Unicode Emoji (Session 2026/05-27)

**Issue**: POST body with emoji causes Unicode errors on some platforms.

**Fix**: Use GET query params for emoji:
```bash
curl -s "https://api.telegram.org/bot<BOT_TOKEN>/sendMessage?chat_id=CHAT_ID&text=🔮✨"
```

Instead of POST body, which fails with certain UTF-8 sequences.

---

## Production Checklist

- [ ] Verify robots.txt compliance (ELLE allows scraping)
- [ ] Implement rate limiting (2+ second delays between requests)
- [ ] Set proper User-Agent headers (anti-bot protection)
- [ ] Handle HTTP 429/503 errors gracefully
- [ ] Respect `article:modified_time` for content freshness
- [ ] Configure Telegram Bot Token
- [ ] Add bot to target channel as admin
- [ ] Test cronjob execution

## Log File

All execution logs are written to: `/tmp/zodiac-daily.log`

Example log format:

```
[2026-05-26 06:22:37] ============================================================
[2026-05-26 06:22:37] 🎯 開始執行雙子座運勢抓取
...
[2026-05-26 06:22:37] ✅ 任務完成！
```

## Maintenance Notes

- ELLE site may restructure — check the script weekly for schema changes
- Cron job should log failures to `/tmp/zodiac-daily.log` for debugging
- Consider proxy rotation if scale increases (not currently implemented)

## Related Skills

- [`scrapling`](../scrapling/SKILL.md) - Production-grade scraping with anti-bot
- [`telegram-bot-setup`](../telegram-bot-setup/SKILL.md) - WSL deployment patterns
- [`felo-web-fetch`](../felo/web-fetch/SKILL.md) - Alternative extraction API

## Related Files

- Script: `~/.hermes/skills/social-media/zodiac-daily/scripts/gemini-horoscope.py`
- Logs: `/tmp/zodiac-daily.log`
- SKILL: `~/.hermes/skills/social-media/zodiac-daily/SKILL.md`
- References: 
  - [`cronjob-patterns.md`](./references/cronjob-patterns.md) (Cronjob execution patterns)
  - [`token-config-pitfalls.md`](./references/token-config-pitfalls.md) (Token configuration pitfalls — WSL + Telegram Bot)

## Key Pitfall Reminder ⚠️

**Telegram Bot Token is required!** Cannot send messages with just Chat ID. Must configure both:
1. Bot Token from @BotFather  
2. Add bot as channel admin

See [`references/cronjob-patterns.md`](./references/cronjob-patterns.md) for execution patterns and WSL-specific notes.

## 🐛 Key Lessons from Session (2026/05-27) ⚡

| 問題類型 | 症狀 | 解決方案 |
|----------|------|----------|
| **Token Masking** (`***`) | Telegram HTTP 400 Bad Request | ✅ 使用完整 Token，避免 `***` 佔位符號 |
| **Variable Name Conflict** | Python `fetch_url` function vs URL variable clash | ✅ 重命名為 `url` 變數 |
| Timeout Too Long (30s) | Script hangs on slow URLs | ✅ 縮短至 15s timeout |\n\n---

## 🆕 Skill Library Updates (2026/05-27) ⚡

**Web Fetch & Scraping Skill Updated**:
- ✅ `web-fetch-and-scraping` skill v2.0 updated with user conciseness preferences
- ✅ WSL curl fallback pattern documented (Chrome exit → terminal mode)
- ✅ GitHub as primary docs source for new projects (vs Hacker News)
- ✅ AI News Aggregation pattern captured in memory

See `~/.hermes/skills/software-development/web-fetch-and-scraping/SKILL.md` for full details.

---

## Related Skills

Always check these pitfalls when modifying the script! See [`references/token-config-pitfalls.md`](./references/token-config-pitfalls.md) for detailed guidance.

---\n\n## Related Skills

When running via `cronjob run` or automated schedule, output follows this structured format:

```json
{
  "status": "completed|failed",
  "timestamp": "2026-05-27T06:00:00+08:00",
  "source": "ELLE.tw",
  "astro_sign": "Gemini / 雙子座",
  "data_extracted": {
    "luck_number": 6,
    "luck_color": "淺海藍",
    "luck_direction": "西北方向",
    "luck_time": "7:00-8:00am",
    "luck_sign": "天蠍座",
    "description": "情緒較低，生活的挫折讓你心灰意懶。"
  },
  "telegram_delivery": {
    "sent": true,
    "chat_id": "8798582756",
    "format": "markdown_v3"
  }
}
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v2.0 | 2026-05-27 | Initial release - basic horoscope extraction |
| **v3.0** | **2026-05-27** | **+ User preferences (中文優先，簡潔直接)**<br>+ **Structured cronjob output format**<br>+ **WSL zero-dependency pattern**<br>+ **Telegram API emoji query params fix**<br>+ **References directory support files** |

---

## Related Skills

- [`scrapling`](../scrapling/SKILL.md) - Production-grade scraping with anti-bot
- [`telegram-bot-setup`](../telegram-bot-setup/SKILL.md) - WSL deployment patterns
- [`felo-web-fetch`](../felo/web-fetch/SKILL.md) - Alternative extraction API

## Related Files

- Script: `~/.hermes/skills/social-media/zodiac-daily/scripts/gemini-horoscope.py`
- Logs: `/tmp/zodiac-daily.log`
- SKILL: `~/.hermes/skills/social-media/zodiac-daily/SKILL.md`
- References: 
  - [`cronjob-patterns.md`](./references/cronjob-patterns.md) (Cronjob execution patterns)
  - [`token-config-pitfalls.md`](./references/token-config-pitfalls.md) (Token configuration pitfalls — WSL + Telegram Bot)

## Key Pitfall Reminder ⚠️

**Telegram Bot Token is required!** Cannot send messages with just Chat ID. Must configure both:
1. Bot Token from @BotFather  
2. Add bot as channel admin

See [`references/cronjob-patterns.md`](./references/cronjob-patterns.md) for execution patterns and WSL-specific notes.