# 🔧 Troubleshooting Guide
## Zodiac-Daily: Common Issues & Solutions

**Project:** zodiac-daily  
**Last Updated:** 2026-05-29  

---

## 🎯 Quick Start (When Something Goes Wrong)

### Issue #1: Script Not Running
```bash
# Check Python version
python3 --version  # Should be 3.10+

# Check script permissions
ls -la scripts/gemini-horoscope.py  # Should show 'x' for executable

# Make executable if needed
chmod 755 scripts/gemini-horoscope.py

# Run with verbose output
python3 scripts/gemini-horoscope.py --verbose 2>&1
```

### Issue #2: Telegram Push Failed
```bash
# Test API access directly
curl "https://api.telegram.org/bot[TOKEN]/getMe"

# Check Chat ID format (must include -100 for supergroups)
echo "chat_id=-10018798582756"  # Not chat_id=123456789

# Verify token in script line ~14
grep -n "TELEGRAM_BOT_TOKEN" scripts/gemini-horoscope.py
```

### Issue #3: GitHub Push Failed
```bash
# Check remote URL
git remote -v

# Update if needed
git remote set-url origin https://github.com/jomoeess-cell/zodiac-daily.git

# Push with tags
git push -u origin master --tags
```

---

## 📁 Common Error Messages & Solutions

### Git Errors

#### "fatal: repository not found"
**Cause:** Wrong GitHub username or repository name  
**Solution:**
```bash
git remote set-url origin https://github.com/jomoeess-cell/zodiac-daily.git
git push -u origin master --tags
```

#### "remote: Repository not found"
**Cause:** 
- Repository doesn't exist on GitHub yet, OR
- You cloned a fork but pushed to wrong branch  
**Solution:** Create repo first at https://github.com/new

---

### Python Runtime Errors

#### "ModuleNotFoundError: No module named 'requests'"
**Problem:** Script expects requests package  
**Solution (WSL with limited sudo):**
```bash
# Option A: Install system-wide (may require sudo)
pip3 install requests

# Option B: Use stdlib only (already implemented in gemini-horoscope.py)
python3 scripts/gemini-horoscope.py  # Should work without dependencies
```

#### "Permission denied" when running script
**Solution:**
```bash
chmod 755 scripts/*.py
python3 scripts/gemini-horoscope.py
```

---

### Telegram API Errors

#### "401 Unauthorized"
**Cause:** Invalid or expired bot token  
**Solution:**
1. Check line ~14 in `scripts/gemini-horoscope.py`
2. Regenerate token from @BotFather on Telegram
3. Update script file

#### "Chat not found" / Invalid Chat ID
**Cause:** Wrong chat ID format or invalid channel  
**Solution:**
- Format: `-100xxxxxxxxxxx` for supergroups (channels/groups)
- Format: `xxxxxxxxxxxx` for personal chats
- Verify by sending test message via curl

---

### GitHub API Errors

#### "403 Forbidden" on push
**Cause:** Invalid or expired Personal Access Token  
**Solution:**
```bash
# Check if token is still valid
curl -H "Authorization: token YOUR_TOKEN" \
  https://api.github.com/user

# Get new token if needed
# https://github.com/settings/tokens
```

---

## 🌐 API Endpoint Troubleshooting

### Gemini Horoscope API

#### URL Format
```bash
BASE_URL="https://share.google/u/schedule/daily/horoscope?target=en&horoscope_date={DATE}"
curl -s "$BASE_URL" | head -50
```

#### Timeout Issues (15s recommended)
**Problem:** API takes too long (>30s)  
**Solution:** Script already uses 15s timeout (line ~20 in gemini-horoscope.py)

#### HTML Parsing Failures
**Problem:** Content changed, selector doesn't match  
**Debug:**
```bash
curl -s "$BASE_URL" | grep -o '<div[^>]*class="[^"]*horoscope[^"]*"[^>]*>[^<]*</div>' | head -5
```

---

### Telegram Bot API

#### Get Me Endpoint (Verify Token)
```bash
TOKEN="your_token_here"
curl -s "https://api.telegram.org/bot$TOKEN/getMe" | jq .
# Expected: {"ok":true,"result":{"is_bot":true,"id":123456789}}
```

#### Send Test Message (Verify Chat ID)
```bash
curl -s "https://api.telegram.org/bot$TOKEN/sendMessage\
  -d chat_id=-10018798582756\
  -d text=✅ Test message from zodiac-daily"
# Expected: {"ok":true,"result":{"message_id":328}}
```

---

## 📊 Log File Analysis

### Check Cron Job Execution
```bash
# View recent log entries
tail -50 /tmp/zodiac-daily.log

# Check for errors (case insensitive)
grep -i "error\|exception" /tmp/zodiac-daily.log

# Count successful runs
grep "✅ 推送成功" /tmp/zodiac-daily.log | wc -l

# View last 10 entries with timestamps
tail -n 10 /tmp/zodiac-daily.log | grep -E "^\[|Message ID:"
```

### Analyze Failures
```bash
# Extract error lines only
grep -v "^$" /tmp/zodiac-daily.log | grep -v "^{" | grep -iE "error|fail" > /tmp/errors.txt
cat /tmp/errors.txt

# Count errors by hour
grep -oP '^\[\K[0-9:]+(?=-)' /tmp/zodiac-daily.log | sort | uniq -c | sort -rn | head -10
```

---

## 🔐 Security Troubleshooting

### Token Leak Detection
```bash
# Check if tokens are in git history (dangerous!)
git log --all --full-history -S "GEMINI_API_TOKEN" --oneline
git log --all --full-history -S "TELEGRAM_BOT_TOKEN" --oneline

# If found, immediate actions:
1. Revoke leaked token from provider
2. git filter-branch or BFG Repo-Cleaner to remove from history
3. Change affected API credentials
```

### File Permissions Audit
```bash
# Check sensitive files
ls -la ~/.zodiac-daily.env          # Should be 600 (rw-------)
ls -la scripts/gemini-horoscope.py # Should have execute permission
ls -la README.md LICENSE           # Should be 644 (rw-r--r--)
```

---

## 🛠️ System-Level Troubleshooting

### WSL Environment Issues

#### Python Version Check
```bash
python3 --version  # Should be 3.10+
which python3      # Should point to /usr/bin/python3

# If wrong version:
update-alternatives --config python3
```

#### Git Configuration
```bash
git config --global user.email "jomoeess@gmail.com"
git config --global user.name "Jomo Jomo"

# Verify
git config --list | grep user
```

---

### Cron Job Troubleshooting

#### Check if cron is running
```bash
service cron status
systemctl status cron  # Or cron.service

# Edit crontab
crontab -e
```

#### View cron logs
```bash
grep CRON /var/log/syslog | tail -20
grep zodiac /var/log/syslog | tail -10
```

#### Debug cron jobs (add `sh -x` to see execution)
```bash
# Temporarily enable debug mode
*/5 * * * * sh -x /home/wsl/.hermes/skills/social-media/zodiac-daily/scripts/gemini-horoscope.py >> /tmp/zodiac-debug.log 2>&1
crontab -l > /tmp/new_cron && crontab /tmp/new_cron
```

---

## 📝 Prevention & Best Practices

### Before Each Commit
```bash
# 1. Verify code works locally
python3 scripts/gemini-horoscope.py

# 2. Check no temp files committed
git status        # Should show clean working tree

# 3. Review changes
git diff HEAD     # Preview commit content

# 4. Create informative commit message
git commit -m "feat: Add comprehensive error handling"
```

### Regular Maintenance
```bash
# Clean up old log files (weekly)
find ~/.hermes/skills/social-media/zodiac-daily/ -name "*.log" -mtime +7 -delete

# Update git tags (for releases)
git tag -l | sort -V

# Check for broken links in documentation
grep -r "http" docs/ README.md | grep -v "https://"  # Prefer HTTPS
```

---

## 🆘 When All Else Fails

### Complete Project Reset
```bash
# Backup current state
tar -czf /tmp/zodiac-daily-backup-$(date +%Y%m%d).tar.gz \
  ~/.hermes/skills/social-media/zodiac-daily/

# Fresh clone (if needed)
rm -rf ~/.hermes/skills/social-media/zodiac-daily
git clone https://github.com/jomoeess-cell/zodiac-daily.git ~/.hermes/skills/social-media/zodiac-daily
cd ~/.hermes/skills/social-media/zodiac-daily

# Restore permissions
chmod 755 scripts/*.py
chmod 644 README.md LICENSE CHANGELOG.md docs/* references/*.md

# Verify setup
git log --oneline -5
python3 scripts/gemini-horoscope.py
```

---

## 📞 Getting Help

### Project Resources
- **GitHub Issues:** https://github.com/jomoeess-cell/zodiac-daily/issues
- **Documentation:** `docs/` directory in repository
- **Skill Guide:** `SKILL.md` for Hermes integration

### Debug Mode Commands
```bash
# Full stack trace on error
python3 scripts/gemini-horoscope.py 2>&1 | tee /tmp/debug-output.log

# Network debugging
curl -v "https://share.google/u/schedule/daily/horoscope?target=en&horoscope_date=2026-05-29"

# Telegram debug
curl -v "https://api.telegram.org/bot[TOKEN]/getMe"
```

---

## 📚 Related Documentation

- [`PROJECT-HISTORY.md`](../PROJECT-HISTORY.md) - Complete project history
- [`GIT-OPS.md`](./GIT-OPS.md) - Version control guide
- [`CHANGELOG.md`](../CHANGELOG.md) - Release notes
- `references/token-config-pitfalls.md` - Token configuration

---

*This guide is updated with every issue encountered and resolved.*
