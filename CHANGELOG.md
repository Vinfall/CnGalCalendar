# Changelog

All notable changes to this project will be documented in this file.

## [4.8.1] - 2026-10-23

### 📦 Dependencies

- Bump dependencies
- Bump jdx/mise-action from 5.1.1 to 5.2.1
- Bump ical from 14.2.0 to 14.3.0
- Bump python matrix to 3.14~3.15
- Bump jdx/mise-action from 5.0.1 to 5.1.1
- Bump python matrix to 3.14~3.15-dev
- Bump jdx/mise-action to v5.0.1, pin to hash

### 🛠️ Chores

- Hide uv.lock changelog
- Unset python.compile to allow python 3.15
- Disable persist-credentials in actions/checkout
- Migrate to global templates

## [4.7.3] - 2026-10-04

### 🐛 Fixes

- Strip space before replace
- Delisted games
- Date parse error of index/6214

### 📦 Dependencies

- Bump dependencies
- Bump ical from 14.0.1 to 14.1.1
- Bump dateparser from 1.4.1 to 1.4.2
- Bump ical from 14.0.0 to 14.0.1

### 🎨 Styling

- Ignore CPY rule in ruff

### 🛠️ Chores

- Ubuntu-slim -> ubuntu-26.04

## [4.6.2] - 2026-06-21

### 📦 Dependencies

- Bump actions/checkout from 6 to 7
- Bump ics from 0.8.0.dev0 to 0.8.0.dev1
- Bump requests from 2.30.0 to 2.30.1
- Bump dependencies

### 🎨 Styling

- Lint via ruff

## [4.6.1] - 2026-03-20

### 🚀 Features

- Add inline metadata

### 🐛 Fixes

- Fix: briefIntroduction could be null
caused by index/6734

### 📦 Dependencies

- Bump jdx/mise-action from 3 to 4

### 🎨 Styling

- Re-enable tombi schema.strict
- Tweak tombi schema.strict

### 🛠️ Chores

- Create uv venv when unavailable
- Set cache_key_prefix to avoid cache pollution
- Pip -> uv in dependabot
- Update .gitignore
- Commit .mise.toml

## [4.2.4] - 2026-02-16

### 🐛 Fixes

- Date parse error caused by index/6013

### 🎨 Styling

- Lint via tombi
- Typing
- Mypy -> ty

### 🛠️ Chores

- Ubuntu-latest -> ubuntu-slim
- Disable _INDEX_FILTER

## [4.1.3] - 2025-12-12

### 📦 Dependencies

- Bump python matrix to 3.13~3.14 per PEP 745
- Bump actions/checkout from 5 to 6
- Bump Python Matrix to 3.12~3.14 per PEP 745
- Bump dependencies
- Bump jdx/mise-action from 2 to 3
- Bump actions/checkout from 4 to 5
- Bump Python Matrix to 3.12~3.14-dev as per PEP 745

### 🛠️ Chores

- Add dependency cooldown
- Use native `gh release upload`
- Block index/6087

## [4.0.0] - 2025-03-20

### 🚀 Features

- Upload calendar to release
- Uv run

### 🐛 Fixes

- Typing error
- Relax python version

### 📚 Docs

- Fix link

### 📦 Dependencies

- Mv to pyproject.toml altoghther

### 🎨 Styling

- Rm pylint
- Extend ruff rules to all
- Lint via zizmor

### 🛠️ Chores

- Ignore everything in output/
- Drop pypy3.11 in python matrix
- Update .gitignore
- Migrate to mise
- Reschedule workflow
- Cache pre-built wheels
- Use cached uv
- Adapt to pyproject.toml

## [2.11.3] - 2025-03-20

### 🐛 Fixes

- Metadata

### 📚 Docs

- More keywords in pyproject.toml
- Update todo

### 📦 Dependencies

- Migrate to uv
- Add deps to pyproject.toml

### 🛠️ Chores

- Mute version bump in changelog
- Update metadata in pyproject.toml

## [2.11.2] - 2025-03-20

### 🐛 Fixes

- Break too aggressively
- Handle empty response

### 🛠️ Chores

- Temp block index/5584

## [2.11.0] - 2025-03-20

### 🚀 Features

- Add pyproject.toml

### 📦 Dependencies

- Bump default python version to 3.13

### 🎨 Styling

- Lint

## [2.8.3] - 2025-03-20

### 📚 Docs

- Silent changelog update

## [2.8.2] - 2025-03-20

### 🐛 Fixes

- Regex syntax

## [2.8.1] - 2025-03-20

### 🐛 Fixes

- Date parse error caused by index/5835
- Fix pypy -mpip install

## [2.7.1] - 2025-03-20

### 🐛 Fixes

- Date parse error caused by index/5642

### 📦 Dependencies

- Bump Python Matrix to 3.11~3.13 as per PEP 719

### 🛠️ Chores

- Allow manual test
- Use unique cache key
- Add pypy3.10 to Python Matrix
- Update ref

## [2.5.2] - 2025-03-20

### 🎨 Styling

- Lint

### 🛠️ Chores

- Add ci badge
- Ignore test on docs change
- Cache installed packages

## [2.4.1] - 2025-03-20

### 🐛 Fixes

- Date parse error caused by index/5597

## [2.4.0] - 2025-03-20

### 🚀 Features

- Add git-cliff

### 🛠️ Chores

- Add changelog

## [2.3.2] - 2025-03-20

### 🎨 Styling

- Lint

## [2.3.1] - 2025-03-20

### 📦 Dependencies

- Bump Python Matrix to 3.11~3.13-dev ahead of 3.13-rc1

### 🛠️ Chores

- Add commit msg prefix

## [2.2.0] - 2025-03-20

### 🚀 Features

- Feat: add index filter
This is added to exclude outdated ID, not meant to be misused as
personal blocklist

### 📚 Docs

- Simplify URL

### 📦 Dependencies

- Bump requests from 2.32.2 to 2.32.3
- Bump requests from 2.32.0 to 2.32.2

## [2.0.1] - 2025-03-20

### 🚀 Features

- Fix longstanding last_modified and dtstamp issue once for all

### 🐛 Fixes

- Fix date parse error caused by index/5181
- Fix date parse error caused by index/5140
- Fix date parse error caused by index/3989
- Fix condition
- Fix git diff commit
- Fix set-output deprecation warning

### 🛠️ Chores

- Discard hacky & faulty sed replacement
- Reschedule as no more commit flooding

## [1.2.1] - 2025-03-20

### 🐛 Fixes

- Fix release filename
- Fix ics eol

## [1.2.0] - 2025-03-20

### 🛠️ Chores

- Update ics only if new release is available

## [1.1.2] - 2025-03-20

### 🛠️ Chores

- Ignore tba release
- Update commit message
- Permission

## [1.1.0] - 2025-03-20

### 🚀 Features

- Better handling of release date

### 🛠️ Chores

- Ignore test on output push

## [1.0.0] - 2024-01-15

<!-- generated by git-cliff -->
