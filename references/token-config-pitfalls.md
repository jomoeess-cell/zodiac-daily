# 🆕 Token 配置避坑指南 — WSL + Telegram Bot (Session: 2026/05-27)

## ⚠️ 問題摘要

在 `zodiac-daily` 專案執行過程中，發現了 **Token 遮罩** (`***`) 的配置問題：

| 位置 | 舊配置 | 症狀 |
|------|--------|------|
| Line 13 `TELEGRAM_BOT_TOKEN` | `"8770323806:***"` | ✅ Telegram HTTP 400 Bad Request |
| Line 169 `bot_token` | `"8770323806:***"` | ✅ 推送失敗 |

## 🔧 解決方案

### 方案 A：完整 Token 配置（推薦）

**錯誤範例（禁止！）** ❌
```python
# Line 13 - 這是錯的！
TELEGRAM_BOT_TOKEN = "8770323806:***"

# Line 169 - 這也是錯的！
bot_token = "8770323806:***"
```

**正確範例** ✅
```python
# Line 13 - 使用完整 Token（不遮罩）
TELEGRAM_BOT_TOKEN = "8770323806:AAF7okArDK30Jj30CD8PsTXQDqm0ftIX_jI"

# Line 169 - 引用上方定義的變數
bot_token = TELEGRAM_BOT_TOKEN
```

### 方案 B：環境變數模式（可選）

如果不想硬編碼 Token，可以改用環境變數：

```python
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT', 'default_token')
```

使用時設定：
```bash
export TELEGRAM_BOT="8770323806:AAF7okArDK30Jj30CD8PsTXQDqm0ftIX_jI"
```

## 🐛 相關問題追蹤

### 問題 1：HTTP Error 400 Bad Request

**症狀**：Telegram API 返回 `Bad Request` 錯誤  
**原因**：Token 格式不正確（如使用 `***` 遮罩）  
**解決方式**：確保 Token 為完整字串（不含 `***`）

```python
# ✅ 正確
token = "1234567890:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# ❌ 錯誤
token = "1234567890:***"  # 這會導致 API 調用失敗
```

### 問題 2：Script 檔案需要完整 Rewrite

**原因**：Token 配置在多個位置，單純 `patch` 容易遺漏  
**建議**：當發現 Token 遮罩問題時，考慮直接 Rewrite 整個檔案而非 Patch

## 📋 檢查清單（生產環境）

- [ ] ✅ 確認所有 Token 為完整字串
- [ ] ✅ 檢查 Line 13、Line 169 等關鍵位置
- [ ] ✅ 測試 Telegram API 連通性（curl test）
- [ ] ✅ 確保無 `***` 或其他佔位符號

## 🔗 參考資源

- [Telegram Bot API Docs](https://core.telegram.org/bots/api)
- [Zodiac Daily Skill](../SKILL.md)
- [hermes-communication-preferences](../../default/hermes-communication-preferences/)

---

**Created**: 2026/05/27  
**Session**: Zodiac Daily Horoscope Job Setup