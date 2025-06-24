# 🏆 Badge Readme

> **Automatically display your Credly badges in your GitHub profile README**

[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Ready-blue?logo=github-actions)](https://github.com/features/actions)
[![Python](https://img.shields.io/badge/Python-3.7+-green?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)

![Example Badges](https://github.com/pemtajo/badge-readme/blob/main/blob/screenshot-readme.png?raw=true)

## 📋 Table of Contents

- [About](#about)
- [Why Version 3.0.0?](#why-version-200)
- [Features](#features)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [Testing](#testing)
- [Technical Details](#technical-details)
- [Changelog](#changelog)

## 🎯 About

**Badge Readme** is an open-source GitHub Action that automatically fetches and displays your [Credly](https://www.credly.com/) badges in your GitHub profile README. It's designed to showcase your professional achievements and certifications in a clean, automated way.

### What it does:
- 🔄 **Automatically updates** your README with latest badges
- 📅 **Sorts badges by date** (newest first)
- 🎨 **Clean markdown format** for better compatibility
- ⚡ **Fast and reliable** badge extraction
- 🔧 **Easy to configure** with minimal setup

## 🚀 Why Version 3.0.0?

### The Challenge
Credly recently updated their website with a completely new HTML structure and user interface. This broke the existing badge extraction functionality in version 1.x.x.

### What Changed in Credly
- **New HTML structure** with different class names
- **Dynamic badge loading** (badges load progressively)
- **Updated DOM elements** for badge containers
- **Changed date format** and extraction methods

### Our Solution
Version 3.0.0 completely refactors the badge extraction to work with Credly's new interface:

- ✅ **Automatic badge expansion** - Clicks "See all badges" to load everything
- ✅ **Updated HTML parser** - Works with new class names and structure
- ✅ **Enhanced date extraction** - Handles new date formats
- ✅ **Improved reliability** - Better error handling and fallbacks

## ✨ Features

### 🆕 Version 3.0.0 Features
- **🎯 Smart Badge Extraction**: Automatically expands to show all badges
- **📅 Date-Based Sorting**: Organizes badges by issue date (newest first)
- **🔄 Modern HTML Parser**: Compatible with Credly's new interface
- **📝 Clean Markdown**: Simple, compatible output format
- **💾 Direct File Generation**: Save badges to files programmatically
- **🧪 Comprehensive Testing**: Full test coverage for reliability

### Core Features
- **🔄 Automated Updates**: Runs on schedule via GitHub Actions
- **🎨 Customizable**: Control number of badges and output format
- **🔒 Secure**: Uses public data only, no authentication required
- **📱 Responsive**: Works across different devices and platforms

## 🚀 Quick Start

### 1. Add Badge Section to Your README

Add these comments to your `README.md`:

```markdown
<!--START_SECTION:badges-->
<!--END_SECTION:badges-->
```

### 2. Create GitHub Action Workflow

Create `.github/workflows/update-badges.yml`:

```yaml
name: Update Badges

on:
  schedule:
    # Runs daily at 2 AM UTC
    - cron: "0 2 * * *"
  workflow_dispatch: # Allow manual runs

jobs:
  update-badges:
    name: Update README with Credly Badges
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Update Badges
        uses: pemtajo/badge-readme@main
        with:
          CREDLY_USER: ${{ github.actor }} # Uses your GitHub username
          NUMBER_LAST_BADGES: 10 # Show last 10 badges (0 = all)
```

### 3. Run the Action

Go to your repository → Actions → "Update Badges" → "Run workflow"

That's it! Your badges will appear in your README automatically.

## ⚙️ Configuration

### Available Options

| Parameter | Default | Description | Required |
|-----------|---------|-------------|----------|
| `GH_TOKEN` | - | GitHub access token | Yes* |
| `REPOSITORY` | `username/username` | Target repository | No |
| `CREDLY_USER` | `username` | Your Credly username | No |
| `NUMBER_LAST_BADGES` | `0` | Number of badges to show (0 = all) | No |
| `COMMIT_MESSAGE` | `Updated README with new badges` | Custom commit message | No |

*Only required for non-profile repositories

### Profile Repository Setup

For your profile repository (`username/username`), you don't need `GH_TOKEN`:

```yaml
- name: Update Badges
  uses: pemtajo/badge-readme@main
```

### Other Repository Setup

For other repositories, add your GitHub token to repository secrets:

```yaml
- name: Update Badges
  uses: pemtajo/badge-readme@main
  with:
    GH_TOKEN: ${{ secrets.GH_TOKEN }}
    REPOSITORY: username/username
```

## 💡 Usage Examples

### Basic Usage
```yaml
- uses: pemtajo/badge-readme@main
```

### Custom Configuration
```yaml
- uses: pemtajo/badge-readme@main
  with:
    CREDLY_USER: john_doe
    NUMBER_LAST_BADGES: 5
    COMMIT_MESSAGE: "🎉 Updated with latest certifications"
```

### Programmatic Usage
```python
from credly import generate_sorted_badges_markdown

# Generate badges for specific user
generate_sorted_badges_markdown(
    username="your_credly_username",
    number_badges=10,
    output_file="my_badges.md"
)
```

## 🤝 Contributing

We welcome contributions! This is an open-source project, and your help makes it better for everyone.

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and add tests
4. **Run the test suite**: `python -m unittest discover -v -s tests`
5. **Commit your changes**: `git commit -m 'Add amazing feature'`
6. **Push to the branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Development Setup

```bash
# Clone the repository
git clone https://github.com/pemtajo/badge-readme.git
cd badge-readme

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m unittest discover -v -s tests
```

### Areas for Contribution

- 🐛 **Bug fixes** and error handling improvements
- ✨ **New features** and enhancements
- 📚 **Documentation** improvements
- 🧪 **Test coverage** expansion


### Code Style

- Follow PEP 8 for Python code
- Add docstrings to new functions
- Include tests for new features
- Update documentation as needed

## 🧪 Testing

### Running Tests Locally

```bash
# Run all tests
python -m unittest discover -v -s tests

# Run specific test file
python -m unittest tests.tests -v
```

### Docker Testing

```bash
cd tests
docker-compose build && docker-compose up
```

### Test Coverage

Our test suite covers:
- ✅ **Core functionality** - Badge extraction and parsing
- ✅ **Date handling** - Extraction and sorting
- ✅ **HTML parsing** - New Credly structure compatibility
- ✅ **Error handling** - Edge cases and failures
- ✅ **File operations** - Markdown generation and saving
- ✅ **Integration** - End-to-end workflows

## 🔧 Technical Details

### How It Works

1. **Fetch HTML**: Retrieves the Credly profile page
2. **Expand Badges**: Clicks "See all badges" to load complete list
3. **Parse Structure**: Extracts badge data using new HTML classes
4. **Extract Dates**: Parses issue dates from Portuguese format
5. **Sort Badges**: Orders by date (newest first)
6. **Generate Markdown**: Creates clean, compatible output
7. **Update README**: Commits changes to your repository

### HTML Structure Changes

**Old Structure (v1.x.x):**
```html
<div class="data-table-row">
  <img class="badge-image" src="...">
</div>
```

**New Structure (v3.0.0):**
```html
<div class="settings__skills-profile__edit-skills-profile__badge-card">
  <img class="settings__skills-profile__edit-skills-profile__badge-card__badge-image" src="...">
  <div class="settings__skills-profile__edit-skills-profile__badge-card__issued">
    Issued 22/11/20
  </div>
</div>
```

### Date Format Handling

Dates are extracted from Portuguese format "Issued dd/mm/yy" and converted to sortable format:
- Input: `Issued 22/11/20`
- Parsed: `2020-11-22`
- Sorted: Newest first

## 📋 Changelog

### [3.0.0] - 2024-01-XX

#### 🆕 Added
- Automatic badge expansion ("See all badges" button)
- Date-based sorting (newest first)
- Updated HTML parser for new Credly structure
- Direct file generation methods
- Comprehensive test suite
- Enhanced error handling

#### 🔄 Changed
- Updated HTML class names and parsing logic
- Improved markdown format (removed href links)
- Better performance and reliability
- Enhanced documentation

#### ❌ Removed
- `CREDLY_SORT` parameter (no longer supported by Credly)
- `BADGE_SIZE` parameter (no longer configurable)

### [1.x.x] - Previous Versions
- Basic badge extraction
- Configurable sorting and badge size
- Simple markdown generation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Credly** for providing the badge platform
- **GitHub Actions** for the automation infrastructure[text](about:blank#blocked)
- **Contributors** who help improve this project
- **Open Source Community** for inspiration and support

---

**Made with ❤️ for the open-source community**

If you find this project helpful, please consider giving it a ⭐ star! 