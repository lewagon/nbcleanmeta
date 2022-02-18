
# 0.2.4 (2022-02-16)

### Added

- Inline `"image/svg+xml"` images according to vscode transformation

# 0.2.3 (2022-02-15)

### Fixed

- Only clean `"image/png"` images trailing newline

# 0.2.2 (2022-02-11)

### Added

- Adds a `CHANGELOG.md` file
- Cleans `outputs` `data` `image/*` trailing newline
- Adds tests for `execution_count` cleaning
- Adds tests for `outputs` `data` `image/*` trailing newline cleaning
- Add `run-test` gha

### Changed

- Requires `wagon_common` version `>=0.2.3`
- `execution_count` are now set to `null` instead of `0`
