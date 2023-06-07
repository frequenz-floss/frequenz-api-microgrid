# Frequenz Migrogrid API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

<!-- Here goes notes on how to upgrade from previous versions, including if there are any deprecations and what they should be replaced with -->

## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes

* [Added missing leading `/` to `GetMicrogridMetadata()`'s HTTP endpoint](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/69)

  This bug prevented building the gRPC gateway for the microgrid API.
  This fix should allow the gRPC gateway builds again.
