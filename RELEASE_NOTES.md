# Frequenz Microgrid API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

- The `CanStreamData` RPC has been removed. Users are recommended to check it
  by calling the `StreamComponentData` RPC.

- `frequenz-api-common` has been updated to `v0.3.1`.

- The message `microgrid.Location` has been removed, and
  `frequenz.api.common.location.Location` is being used instead. The `Location`
  message from the common API also has a `country_code` member.

- The following gRPC method has been renamed:
  `StreamComponentData` -> `SubscribeComponentData`

## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
