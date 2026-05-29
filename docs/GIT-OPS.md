# 🗃️ Git Operations Guide
## Zodiac-Daily: Version Control Best Practices

**Project:** zodiac-daily  
**Last Updated:** 2026-05-29  
**Git Status:** Active (master branch)

---

## 📦 Repository Structure

```
~/.hermes/skills/social-media/zodiac-daily/
├── .git/                          # Git metadata
├── .gitignore                     # Ignore rules
├── .gitattributes                 # File permissions
├── LICENSE                        # MIT License
├── README.md                      # Usage guide (2549B)
├── CHANGELOG.md                   # Version history (854B)
├── PULL_REQUEST_TEMPLATE.md       # PR template (1224B)
├── SKILL.md                       # Hermes skill docs (12KB)
├── references/                    # Reference documents
│   └── token-config-pitfalls.md   # Token config notes
├── scripts/                       # Automation scripts
│   └── gemini-horoscope.py        # Main script (4.7KB, executable)
└── docs/                          # Project history & guides
    ├── PROJECT-HISTORY.md         # Comprehensive history (this file's sibling)
    └── GIT-OPS.md                 # ← You are here
```

---

## 🏷️ Tagging Convention

### Semantic Versioning (SemVer)

| Major | Minor | Patch | Meaning | Example |
|-------|-------|-------|---------|---------|
| 0     | x     | y     | Backwards compatible features | v0.3.0 |
| -1    | Initial release with core functionality | v0.1.0 | Core horoscope automation |
| -2    | Added documentation & examples | v0.2.0 | README.md, usage guide |
| -3    | Organized structure + permissions | v0.3.0 | .gitattributes, licenses |

### Tag Format
```bash
git tag v0.x.y -a "Release description" -m "Commit message"
```

### Creating Tags
```bash
# Create annotated tag (recommended for releases)
git tag v0.3.1 -a "Fix: Add log rotation script" -m "Added automated cleanup"

# Push tags to remote
git push origin master --tags
```

---

## 📝 Commit Message Convention

### Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
| Type | Example | Description |
|------|---------|-------------|
| feat | `feat: Add new feature` | New functionality |
| fix | `fix: Bug fix` | Bug resolution |
| docs | `docs: Update README.md` | Documentation |
| style | `style: Format code` | Code formatting |
| refactor | `refactor: Improve structure` | Code restructuring |
| perf | `perf: Optimize API calls` | Performance improvement |
| test | `test: Add unit tests` | Test addition |
| chore | `chore: Update dependencies` | Build tasks |

### Examples
```bash
# Good commit messages
git commit -m "feat: Add log rotation automation"
git commit -m "fix: Correct GitHub token path in script"
git commit -m "docs: Update README.md with usage examples"
git commit -m "chore: Add .gitattributes for file permissions"

# Bad commit messages (avoid these)
git commit -m "Update"                 # Too vague
git commit -m "Fix stuff"              # What stuff?
git commit -m "Add new feature here"   # What feature?
```

---

## 🔀 Branch Management

### Main Branches
| Branch | Purpose | Push Permission |
|--------|---------|-----------------|
| `master` | Production-ready code | ✅ Yes (protected) |
| `develop` | Integration branch | ⚠️ Team only |
| `feature/*` | New features | ❌ No (squash to master) |

### Branch Flow (Current Project)
```bash
# Since this is a personal project, we use single-branch workflow:
1. Feature development on master branch
2. Test locally
3. Commit with descriptive message
4. Create semantic version tag
5. Push to GitHub
```

---

## 🚀 Deployment Workflow

### Standard Release Process
```bash
# 1. Update code
nano scripts/gemini-horoscope.py

# 2. Verify changes
git status
git diff

# 3. Commit with message
git add .
git commit -m "feat: Add multi-zodiac support"

# 4. Create tag (if releasing)
git tag v0.x.y -a "Release description" -m "Release notes"

# 5. Push to GitHub
git push origin master --tags

# 6. Verify deployment
curl "https://api.github.com/repos/jomoeess-cell/zodiac-daily/commits?per_page=1"
```

---

## 🧪 Testing Before Commit

### Pre-commit Checklist
- [ ] Code runs without errors: `python3 scripts/gemini-horoscope.py`
- [ ] No new warnings in logs
- [ ] Documentation updated (README.md, CHANGELOG.md)
- [ ] .gitignore rules respected (no temp files committed)
- [ ] File permissions correct (`chmod 755` for scripts, `644` for docs)

### Test Commands
```bash
# Test script locally
python3 ~/.hermes/skills/social-media/zodiac-daily/scripts/gemini-horoscope.py

# Check file permissions
ls -la scripts/ docs/ README.md LICENSE CHANGELOG.md

# Verify git status (should be clean before commit)
git status

# Preview changes
git diff HEAD

# Push and verify on GitHub
git push origin master --tags
curl "https://api.github.com/repos/jomoeess-cell/zodiac-daily" | grep html_url
```

---

## 🐛 Issue Management

### Current Known Issues
| ID | Title | Status | Notes |
|----|-------|--------|-------|
| #1 | GitHub Token Configuration | ✅ Resolved | Moved to token-based auth |
| #2 | Repository Migration | ✅ Resolved | Updated remote URL |
| #3 | Log Rotation | 🚧 In Progress | Recommend /var/log/ or logrotate |

### Issue Template (for future)
```markdown
## Bug Report

**Description:**  
[What went wrong?]

**Steps to Reproduce:**  
1. [First step]  
2. [Second step]  
3. [What happens]

**Expected Behavior:**  
[What should happen?]

**Actual Behavior:**  
[What actually happened?]

**Environment:**  
- Python: `python3 --version`  
- OS: `uname -a`  
- WSL Version: `wsl --version`  

**Logs:**  
```bash
tail -50 /tmp/zodiac-daily.log
```

**Additional Context:**  
[Any relevant information?]
```

---

## 📦 Pull Request Workflow (for collaboration)

### PR Template (PULL_REQUEST_TEMPLATE.md)
```markdown
## Description

[Describe your changes]

## Type of Change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## How Has This Been Tested?

[Describe your testing steps]

## Screenshots (if applicable)

[Add screenshots if needed]

## Checklist

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have reviewed the project's security guidelines

## Related Issues

Closes #[issue_number]
```

---

## 🔐 Security Best Practices

### Token Management
```bash
# ❌ NEVER commit tokens to Git
echo "GEMINI_API_TOKEN=xyz" >> .env  # DON'T DO THIS!

# ✅ DO store tokens in .env (not committed)
nano ~/.zodiac-daily.env       # Add to .gitignore
export GEMINI_API_TOKEN=$(cat ~/.zodiac-daily.env | grep GEMINI | cut -d= -f2)
```

### File Permissions Check
```bash
# Verify permissions are correct
ls -la README.md LICENSE CHANGELOG.md    # Should be 644 (rw-r--r--)
ls -la scripts/*.py                       # Should be 755 (rwxr-xr-x)
ls -la ~/.zodiac-daily.env                # Should be 600 (rw-------)
```

---

## 📊 Monitoring & Maintenance

### Daily Checks
```bash
# Check last run status
tail -10 /tmp/zodiac-daily.log

# Check cron job execution
grep zodiac /var/log/syslog | tail -5

# Verify GitHub commit activity
curl "https://api.github.com/repos/jomoeess-cell/zodiac-daily/commits?per_page=5" | jq '.[].commit.message'
```

### Log Rotation (Recommended)
```bash
# Add to /etc/logrotate.d/zodiac-daily
/tmp/zodiac-daily.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 644 root root
}
```

---

## 📚 References

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Tags Documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/annotated-tags-and-lightweight-tags)
- [Semantic Versioning Specification](https://semver.org/)
- [Python Style Guide - PEP 8](https://peps.python.org/pep-0008/)

---

*This guide is part of the zodiac-daily project documentation.*
