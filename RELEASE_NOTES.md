# Frequenz Microgrid API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

- The minimum supported version of `protobuf` was bumped to 5.28.1 and to 1.66.1 for `grpcio`. Make sure to update your dependencies accordingly.
- The `AddComponentBoundsRequest.validity_duration` field was replaced by `AddComponentBoundsRequest.request_lifetime` to match the fields in `SetComponentPowerActiveRequest` and `SetComponentPowerReactiveRequest`. The default value was also changed from 5 to 60 seconds.

## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
