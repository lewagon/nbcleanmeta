# 0.2.8 (2025-03-27)

### Added

- Removes the `id`, `outputId` and `colab` cell metadata (created by Colab)
- Removes empty cell metadata created by notebook>7.0.0 when one has the Notebook Tools sidepane open:
  - `editable` cell metadata (configurable on the cli)
  - `tags` cell metadata if empty (always)
  - `slideshow.slide_type` cell  metadata if empty (always)
  - `slideshow` cell  metadata if empty (always)
- Removes `execution` cell metadata created by jupyterlab-execute-time

# 0.2.7 (2025-01-27)

### Updated

- Removes the GHA publishing the package to Gemfury on merge
- Updates instructions to install from GitHub public repo

# 0.2.6 (2022-08-19)

### Added

- Removes the `vscode` cell metadata

# 0.2.5 (2022-06-14)

### Added

- Removes `id` cell key

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
