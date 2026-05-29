# 🗂️ Git 文檔檢索目錄 (Index)
## Zodiac-Daily: Complete Documentation Index & Retrieval System

**Project:** [zodiac-daily](https://github.com/jomoeess-cell/zodiac-daily.git)  
**Last Updated:** 2026-05-29  
**Status:** v0.5.1 Released  

---

## 📚 文檔分類總覽

```bash
🗂️ zodiac-daily Git Documentation Structure
│
├─ 🟢【實用性高 - 立即應用】 (HIGH PRIORITY)
│   ├─ 🧭 快速開始指南 → README.md
│   ├─ 🔐 Token 管理規範 → references/token-config-pitfalls.md  
│   └─ ⚙️ Git Ops 標準流程 → GIT-OPS.md
│
├─ 🟡【中階參考 - 按需查詢】 (MEDIUM PRIORITY)
│   ├─ 📜 專案歷史紀錄 → docs/PROJECT-HISTORY.md
│   ├─ 🔧 Capabilities 總覽 → docs/GIT-CAPABILITIES.md
│   └─ 🐛 Troubleshooting → docs/TROUBLESHOOTING.md
│
└─ 🔵【進階拓展 - 長期規劃】 (ADVANCED USE CASES)
    ├─ 🧪 Testing 策略 → [待建立]
    ├─ 🤖 CI/CD Pipeline → [待建立]
    └─ 📈 Analytics 儀表板 → [待建立]
```

---

## 🟢【實用性高 - 立即應用】 HIGH PRIORITY

### 1. README.md - 快速開始指南

**🎯 用途：** 新用戶入門、快速使用說明  
**⚡ 適用時機：** 第一次接觸專案、需要快速執行腳本時  
**📄 大小：** ~2.5KB  

**📖 包含內容：**
- ✅ 專案功能簡介
- ✅ 快速開始 (Quick Start) 命令
- ✅ 基本使用範例
- ✅ 檔案結構說明

**🔗 快速連結：** [README.md](../../README.md)

---

### 2. references/token-config-pitfalls.md - Token 管理規範

**🎯 用途：** 防止 Token 洩漏的安全規範  
**⚡ 適用時機：** 配置 API Token、環境變數設定前必讀  
**📄 大小：** ~1.5KB  

**📖 包含內容：**
- ✅ `.gitignore` 規則說明
- ✅ Token 配置最佳實踐
- ✅ `.env` 檔案管理策略
- ✅ WSL 環境限制與對策

**⚠️ 重要提醒：**  
```bash
❌ NEVER commit tokens to Git!
✅ DO store in ~/.zodiac-daily.env (gitignored)
```

**🔗 快速連結：** [token-config-pitfalls.md](references/token-config-pitfalls.md)

---

### 3. GIT-OPS.md - Git Ops 標準流程

**🎯 用途：** Git 版本控制操作規範  
**⚡ 適用時機：** 每次 commit、release、branch 切換前參考  
**📄 大小：** ~8.3KB  

**📖 包含內容：**
- ✅ SemVer 標籤規範 (v0.x.y)
- ✅ Commit 訊息格式（Conventional Commits）
- ✅ Branch 管理策略
- ✅ Deployment Workflow
- ✅ Testing Before Commit Checklist
- ✅ Issue Management 模板
- ✅ Pull Request Template
- ✅ Security Best Practices
- ✅ Monitoring & Maintenance

**⚙️ 核心命令範例：**
```bash
# Release workflow
git tag v0.x.y -a "Release description" -m "Release notes"
git push origin master --tags

# Commit with proper message
git commit -m "feat: Add new feature"  
git commit -m "fix: Correct GitHub token path"
git commit -m "docs: Update README.md"
```

**🔗 快速連結：** [GIT-OPS.md](./GIT-OPS.md)

---

## 🟡【中階參考 - 按需查詢】 MEDIUM PRIORITY

### 4. docs/PROJECT-HISTORY.md - 專案歷史紀錄

**🎯 用途：** 了解專案演進歷程、決策背景  
**⚡ 適用時機：** 需要了解「為什麼這樣做」、長期維護時  
**📄 大小：** ~8KB (311 行)  

**📖 包含內容：**
- ✅ 版本迭代歷史（v0.1.0 → v0.5.1）
- ✅ Feature 演進軌跡
- ✅ Issue 追蹤紀錄
- ✅ Lessons Learned 經驗教訓
- ✅ 歸檔文件清單與說明

**💡 典型查詢：**
- 「為什麼使用 HTTPS + Token 而非 SSH？」
- 「專案的初始化決策過程是什麼？」
- 「過往有哪些 Bug fix ？」

**🔗 快速連結：** [docs/PROJECT-HISTORY.md](./docs/PROJECT-HISTORY.md)

---

### 5. docs/GIT-CAPABILITIES.md - Capabilities 總覽

**🎯 用途：** Git 倉庫功能能力完整說明  
**⚡ 適用時機：** 評估 Git 倉庫能協助的工作、版本控制策略規劃  
**📄 大小：** ~10.5KB (437 行)  

**📖 包含內容：**
- ✅ 7 大核心功能解析（版本控制、協作、專案管理、自動化、除錯、知識管理、腳本支援）
- ✅ 針對 zodiac-daily 的實際應用場景
- ✅ 建議的下一步擴展方向
- ✅ 學習路徑建議（初學者/進階/專家）

**🎯 核心價值：**
```bash
✅ 版本快照 - 隨時保存開發進度 (v0.x.y 標籤)
✅ 除錯追蹤 - 查看 gemini-horoscope.py 變更歷程
✅ 效能分析 - 統計 cron job 執行記錄與 API 時間
✅ 安全審查 - .gitignore 確保 Token 不洩漏  
✅ 知識累積 - docs/ 完整記錄專案歷史與決策
```

**🔗 快速連結：** [docs/GIT-CAPABILITIES.md](./docs/GIT-CAPABILITIES.md)

---

### 6. docs/TROUBLESHOOTING.md - 問題排查指南

**🎯 用途：** 常見問題解決、錯誤處理  
**⚡ 適用時機：** 遇到 Git/專案執行問題時快速查找解決方案  
**📄 大小：** ~8.5KB (358 行)  

**📖 包含內容：**
- ✅ Python 版本檢查
- ✅ Git 配置設定
- ✅ Cron Job Troubleshooting
- ✅ 除錯模式啟用（`sh -x`）
- ✅ 定期維護建議
- ✅ 完全重設流程（Backup + Fresh Clone）

**🔧 常見問題速查：**
| 問題類型 | 解決方案命令 |
|---------|--------------|
| Python 版本錯誤 | `update-alternatives --config python3` |
| Cron job 不執行 | `service cron status`, `crontab -e` |
| 程式碼回滾 | `git reset --soft HEAD~1` |

**🔗 快速連結：** [docs/TROUBLESHOOTING.md](./docs/TROUBLESHOOTING.md)

---

## 🔵【進階拓展 - 長期規劃】 ADVANCED USE CASES

### 7. LICENSE - MIT 開源授權

**🎯 用途：** 專案授權條款  
**⚡ 適用時機：** 引用專案、貢獻程式碼時了解授權範圍  
**📄 大小：** ~1KB  

**🔗 連結：** [LICENSE](../../LICENSE)

---

### 8. CHANGELOG.md - 版本更新記錄

**🎯 用途：** Release 歷史、變更追蹤  
**⚡ 適用時機：** 需要了解版本變更內容、升级前參考  
**📄 大小：** ~1KB  

**📊 當前版本：**
- v0.5.1 - Git Capabilities & Changelog Update ✅ (Latest)
- v0.5.0 - Complete Git Capabilities Guide
- v0.4.0 - Documentation Archive Pattern
- ... → v0.1.0

**🔗 連結：** [CHANGELOG.md](../../CHANGELOG.md)

---

### 9. PULL_REQUEST_TEMPLATE.md - PR 模板

**🎯 用途：** Collaboration 時的 PR 撰寫規範  
**⚡ 適用時機：** 多人協作、Code Review 前參考模板  
**📄 大小：** ~1.2KB  

**📖 包含內容：**
- ✅ Description（變更說明）
- ✅ Type of Change（Bug fix / Feature / Breaking change）
- ✅ Testing Checklist
- ✅ Screenshots（如適用）
- ✅ Code Review Checklist

**🔗 連結：** [PULL_REQUEST_TEMPLATE.md](../../PULL_REQUEST_TEMPLATE.md)

---

### 10. SKILL.md - Hermes Skill 文檔

**🎯 用途：** Hermes Agent 技能整合說明  
**⚡ 適用時機：** 使用 Hermes、了解技能功能時參考  
**📄 大小：** ~12KB  

**📖 包含內容：**
- ✅ Skill 用法與特性
- ✅ API Endpoints
- ✅ Git Operations（PR workflow）

**🔗 連結：** [SKILL.md](../../SKILL.md)

---

### 11. .gitignore - 忽略規則

**🎯 用途：** 排除敏感文件、暫存檔案  
**⚡ 適用時機：** Commit 前檢查是否誤提交、配置環境時參考  
**📄 大小：** ~0.5KB  

```bash
# Core rules
*.log      # Cron output logs
*.tmp      # Temp files
tmp/       # Temporary directories
temp/      # Build artifacts

# Environment (sensitive)
.env
.zodiac-daily.env
```

**🔗 連結：** [.gitignore](../.gitignore)

---

### 12. .gitattributes - 檔案權限設定

**🎯 用途：** 統一 LF/CRLF、executable 設定  
**⚡ 適用時機：** 跨平台開發、避免格式問題時參考  
**📄 大小：** ~0.8KB  

```bash
*.md filter=lfs diff=lfs merge=lfs -text
*.py text eol=lf
*.sh text eol=lf executable=true
```

**🔗 連結：** [.gitattributes](../.gitattributes)

---

## 📊 文檔優先級總覽表

| 文件 | 實用性評分 | 適用頻度 | 推薦程度 | 快速連結 |
|------|----------|---------|---------|---------|
| **README.md** | ⭐⭐⭐⭐⭐ | 高 | ✅ 必讀 | [README.md](../../README.md) |
| **GIT-OPS.md** | ⭐⭐⭐⭐⭐ | 高 | ✅ 必讀 | [GIT-OPS.md](./GIT-OPS.md) |
| **token-config-pitfalls.md** | ⭐⭐⭐⭐⭐ | 中 | ✅ 必讀 | [references/token-config-pitfalls.md](references/token-config-pitfalls.md) |
| **GIT-CAPABILITIES.md** | ⭐⭐⭐⭐ | 低→中 | 🟡 按需 | [docs/GIT-CAPABILITIES.md](./docs/GIT-CAPABILITIES.md) |
| **PROJECT-HISTORY.md** | ⭐⭐⭐ | 低 | 🟡 長期維護 | [docs/PROJECT-HISTORY.md](./docs/PROJECT-HISTORY.md) |
| **TROUBLESHOOTING.md** | ⭐⭐⭐⭐ | 中 | ✅ 出問題時查 | [docs/TROUBLESHOOTING.md](./docs/TROUBLESHOOTING.md) |
| CHANGELOG.md | ⭐⭐ | 低 | 🟡 升级前看 | [CHANGELOG.md](../../CHANGELOG.md) |
| PULL_REQUEST_TEMPLATE.md | ⭐⭐⭐ | 中（協作時） | 🟡 PR 撰寫參考 | [PULL_REQUEST_TEMPLATE.md](../../PULL_REQUEST_TEMPLATE.md) |
| SKILL.md | ⭐⭐⭐ | 低（Hermes 用戶） | 🟡 Hermes 整合 | [SKILL.md](../../SKILL.md) |

---

## 🔍 檢索快捷指令 (Search Patterns)

### 常用查詢場景

| 查詢目標 | 建議文件 | 關鍵字搜尋 |
|---------|---------|-----------|
| 快速開始使用 | README.md | `Quick Start` / `Usage` |
| Token 配置規範 | token-config-pitfalls.md | `.gitignore` / `.env` / `TOKEN` |
| Commit 訊息規範 | GIT-OPS.md | `Commit Message` / `feat:` / `fix:` |
| Release 流程 | GIT-OPS.md | `Deployment Workflow` / `git tag` |
| 除錯問題 | TROUBLESHOOTING.md | `error:` / `check` / `verify` |
| Git 能力總覽 | GIT-CAPABILITIES.md | `capability` / `workflow` / `use case` |
| 專案演進歷程 | PROJECT-HISTORY.md | `v0.x.y` / `evolution` / `issue` |

### Git 命令檢索 (Quick Access)

```bash
# 🔍 搜尋 README 中的快速開始指南
grep -i "quick start\|usage" ~/.hermes/skills/social-media/zodiac-daily/README.md

# 🔍 搜尋 Token 配置規範
grep -r "GEMINI_API_TOKEN\|.env" references/token-config-pitfalls.md

# 🔍 搜尋 Git 標籤規範
grep -A5 "git tag v0.x.y" docs/GIT-OPS.md

# 🔍 搜尋 Commit 訊息範例
grep -i "\"feat:\|\"fix:\"\" ~/.hermes/skills/social-media/zodiac-daily/docs/GIT-OPS.md

# 🔍 查找所有 Markdown 文檔
find ~/.hermes/skills/social-media/zodiac-daily/ -name "*.md" | sort
```

---

## 🗂️ 建議的目錄結構 (Proposed Structure)

### 當前狀態 ✅
```bash
~/.hermes/skills/social-media/zodiac-daily/
├── .git/
├── .gitignore                     # ✅ Core rules
├── .gitattributes                  # ✅ File permissions
├── LICENSE                        # ✅ MIT License
├── README.md                      # ✅ Quick Start Guide (2.5KB)
├── CHANGELOG.md                   # ✅ Release notes (1KB)
├── PULL_REQUEST_TEMPLATE.md        # ✅ PR template (1.2KB)
├── SKILL.md                       # ✅ Hermes skill docs (12KB)
├── references/
│   └── token-config-pitfalls.md   # ✅ Token management guide
├── scripts/
│   └── gemini-horoscope.py        # ✅ Main script (4.7KB)
└── docs/
    ├── PROJECT-HISTORY.md         # ✅ Project evolution (8KB)
    ├── GIT-OPS.md                 # ✅ Git operations guide (8.3KB)
    ├── TROUBLESHOOTING.md         # ✅ Troubleshooting guide (8.5KB)
    ├── GIT-CAPABILITIES.md        # ✅ Capabilities overview (10.5KB)
    └── 05-git-capabilities.md      # ⚠️ Duplicate (可移除)
```

### 建議新增（中長期規劃）⏳
```bash
~/.hermes/skills/social-media/zodiac-daily/
├── .github/
│   ├── workflows/                 # 🟢 CI/CD pipelines
│   │   ├── release.yml            # 🔄 Auto-release on tag push
│   │   └── test.yml               # 🧪 Automated pytest tests
│   └── pull_request_template.md    # 🤖 PR checklist auto-generate
├── tests/                        # 🟢 Unit tests (pytest)
│   ├── __init__.py
│   ├── test_gemini-horoscope.py   # 🧪 Script functionality tests
│   └── test_integration.py        # 🔗 Integration tests
├── docs/
│   ├── API.md                    # 📖 API usage documentation
│   ├── CONTRIBUTING.md           # 👥 Contribution guidelines
│   ├── PERFORMANCE.md            # ⚡ Performance optimization tips
│   └── STYLE_GUIDE.md            # ✨ Code style & best practices
└── .github/                      # 🔵 GitHub-specific docs
    ├── PULL_REQUEST_TEMPLATE.md  # 🤝 PR review checklist
    └── CODE_OF_CONDUCT.md        # ⚖️ Community guidelines
```

---

## 🎯 快速檢索指南 (Quick Retrieval Guide)

### Scenario-based 檢索流程

#### 🔹 **Scenario 1: 新用戶第一次使用**
```bash
1. 閱讀 README.md → "Quick Start" section
2. 配置 Token：閱讀 references/token-config-pitfalls.md
3. 執行腳本：python3 scripts/gemini-horoscope.py
4. 查看結果
```

#### 🔹 **Scenario 2: 開發新功能**
```bash
1. 建立功能分支：git checkout -b feature/new-feature
2. 參考 GIT-OPS.md → "Commit Message Convention"
3. 實作並測試：python3 scripts/gemini-horoscope.py
4. Commit：git commit -m "feat: Add new-feature"
5. Release（可選）：git tag v0.x.y && git push --tags
```

#### 🔹 **Scenario 3: 處理 Bug**
```bash
1. 檢查 TROUBLESHOOTING.md → 查找類似問題
2. 使用 git log -p → 查看變更歷史
3. bisect：git bisect start ... git bisect bad
4. Fix bug 並 commit：git commit -m "fix: Resolve X issue"
```

#### 🔹 **Scenario 4: Release 新版本**
```bash
1. 更新 GIT-OPS.md → "Deployment Workflow"
2. 更新 CHANGELOG.md → 新增版本資訊
3. Create tag：git tag v0.x.y -a "Release description" -m "Release notes"
4. Push tags：git push origin master --tags
```

#### 🔹 **Scenario 5: Token 配置/安全檢查**
```bash
1. 閱讀 references/token-config-pitfalls.md → Security section
2. 確認 .env 檔案已加入 .gitignore
3. chmod ~/.zodiac-daily.env 600
4. Export token from .env file (see GIT-OPS.md)
```

---

## 📝 索引維護說明

### ✅ 當前狀態：基礎文檔齊全

**已有：**
- 🟢 HIGH PRIORITY 文件 × 3（README、GIT-OPS、Token）
- 🟡 MEDIUM PRIORITY 文件 × 4（PROJECT-HISTORY、GIT-CAPABILITIES、TROUBLESHOOTING、CHANGELOG）
- 🔵 ADVANCED 文件 × 2（PULL_REQUEST_TEMPLATE、SKILL.md）

**待新增（中長期）：**
- 🧪 tests/ 測試套件
- 🤖 .github/workflows/ CI/CD
- 📖 API.md API 使用文檔
- 👥 CONTRIBUTING.md 貢獻指南
- ✨ STYLE_GUIDE.md 程式碼規範

---

## 🔗 外部參考連結

| 資源 | 用途 |
|------|------|
| [Git Official Docs](https://git-scm.com/doc) | Git 核心命令與最佳實踐 |
| [GitHub Actions Docs](https://docs.github.com/en/actions) | CI/CD Pipeline 設定 |
| [Semantic Versioning (SemVer)](https://semver.org/) | Release 版本規範 |
| [Conventional Commits](https://www.conventionalcommits.org/) | Commit Message 格式標準 |

---

**🔮 Last Updated:** 2026-05-29  
**Version:** 1.0  
**Author:** Jomo Jomo  

---

*本索引文件旨在幫助快速檢索 Git 倉庫中的相關文檔。優先級標記（🟢/🟡/🔵）代表建議的閱讀順序與適用頻度。*
