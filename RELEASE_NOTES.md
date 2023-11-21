# Frequenz Microgrid API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

- The `CanStreamData` RPC has been removed. Users are recommended to check it
  by calling the `StreamComponentData` RPC.

- The message `microgrid.Location` has been removed, and
  `frequenz.api.common.location.Location` is being used instead. The `Location`
  message from the common API also has a `country_code` member.

- The following gRPC methods have been renamed:
  `StreamComponentData` -> `ReceiveComponentDataStream`
  `AddExclusionBounds`  -> `AddComponentExclusionBounds`
  `AddInclusionBounds`  -> `AddComponentInclusionBounds`
  `SetPowerActive`      -> `SetComponentPowerActive`
  `SetPowerReactive`    -> `SetComponentPowerReactive`
  `Start`               -> `StartComponent`
  `HotStandby`          -> `HotStandbyComponent`
  `ColdStandby`         -> `PutComponentInStandby`
  `Stop`                -> `StopComponent`
  `ErrorAck`            -> `AckComponentError`

- The following gRPC method have been removed: `HotStandby`

- Introduced a dedicated RPC method for listing sensors in the microgrid,
  separating them from the "component" category.

- The RPC parameters have been renamed to be more consistent with the RPC names,
  and with each other.

- The package names have been changed from `frequenz.api.microgrid.<package>` to
  `frequenz.api.microgrid.v1.<package>`. `v1` is the API's major version, and
  will be incremented for breaking changes.

- The common protobuf dependency has been upgraded to `v0.5.0`. The protobuf
  messages returned by the RPCs are now in the `frequenz.api.common.v1` package.
  As a result, all files besides `microgrid.proto` became obsolete, and
  therefore, have been removed.

- The request messages for receiving data streams have now been extended to
  consist of a list of metrics to be streamed. This allows the user to request
  only the metrics they are interested in, instead of receiving all of them.
  If this list is empty, then no data will be streamed, and the service will
  return an error.

## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
