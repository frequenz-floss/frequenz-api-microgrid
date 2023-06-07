# Frequenz Migrogrid API Release Notes

## Summary

Bug fixes.

## Upgrading

None

## New Features

None

## Bug Fixes

* [Added missing leading `/` to `GetMicrogridMetadata()`'s HTTP endpoint](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/69)

  This bug prevented building the gRPC gateway for the microgrid API.
  This fix should allow the gRPC gateway builds again.

* [Bumped `frequenz-api-common` Python dependency](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/67)

  The `frequenz-api-common` submodule was bumped in the previous release but the Python package was forgotten.
