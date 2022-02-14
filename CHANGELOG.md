
# 0.2.2 (2022-02-11)

### Added

- Adds a `CHANGELOG.md` file
- Adds tests for `execution_count` cleaning
- Adds tests for `outputs` `data` `image/*` trailing newline cleaning
- Add `run-test` gha

### Changed

- Requires `wagon_common` version `>=0.2.3`
- `execution_count` are now set to `null` instead of `0`
- Cleans `outputs` `data` `image/*` trailing newline
