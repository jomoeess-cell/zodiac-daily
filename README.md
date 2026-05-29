# 📅 Zodiac Daily - 星座運勢自動推送系統

## 🎯 功能特點

- **雙子座每日運勢**：自動爬取 Gemini 每日星座運勢
- **Telegram 自動推送**：每天早上 6:00 自動推送到 Telegram
- **WSL 零依賴環境**：使用 Python stdlib，無需額外安裝 package

## 📁 專案結構

```
zodiac-daily/
├── scripts/
│   └── gemini-horoscope.py     # 主程式腳本
├── references/
│   ├── token-config-pitfalls.md # Token 配置注意事項
│   └── zodiac-token-config-guide.md # Gemini API token 設定指南
├── SKILL.md                     # Hermes 技能說明
└── README.md                    # 專案說明
```

## 🚀 快速開始

### 1. 設定 Gemini Token

```bash
export GEMINI_API_TOKEN="your_token_here"
```

或使用 `.env` 檔案：
```bash
echo "GEMINI_API_TOKEN=your_token_here" >> ~/.zodiac-daily.env
source ~/.zodiac-daily.env
```

### 2. 測試腳本運作

```bash
python3 scripts/gemini-horoscope.py
```

### 3. 設定每日自動推送 (Cron)

```bash
# 編輯 crontab
crontab -e

# 新增這一行（每天早上 6:00）
0 6 * * * python3 ~/.hermes/skills/social-media/zodiac-daily/scripts/gemini-horoscope.py >> /tmp/zodiac-daily.log 2>&1
```

## 📝 使用方式

### 單次執行

```bash
python3 scripts/gemini-horoscope.py
```

### 查看每日運勢分析輸出

腳本會自動：
- ✅ 爬取 Gemini 今日星座運勢
- ✅ 解析雙子座內容
- ✅ 生成結構化運勢報告（含 emoji、溫度、關鍵詞）

## 📋 輸出格式範例

```markdown
## 🎀 Gemini 每日星座運勢 - 5月29日

### 5.27 (水) 雙子座運勢：⭐️⭐️⭐️⭐️⭐️

> 「親愛的雙子，今日你的靈感如閃電般活躍！創意爆發，但記得平衡理性與感性...」

**關鍵詞**: #靈感爆發 #創意滿分 #社交魅力 #輕度焦慮

### 🌡️ 溫度區間：20-27°C
### 📊 運勢指數：95/100

[推薦文章連結]
```

## ⚠️ 注意事項

- **Token 安全**：請將 token 寫入 `~/.zodiac-daily.env`（加入 `.gitignore`）
- **Log 管理**：輸出檔案已加入 `.gitignore`，不會被上傳
- **時區問題**：腳本使用 UTC+8，自動調整 WSL 時間

## 📚 相關文件

- [`SKILL.md`](./SKILL.md) - Hermes 技能說明與使用方式
- [`references/token-config-pitfalls.md`](./references/token-config-pitfalls.md) - Token 配置注意事項
- [`scripts/gemini-horoscope.py`](./scripts/gemini-horoscope.py) - 主程式腳本

---

**Version**: 0.1.0  
**License**: MIT License
