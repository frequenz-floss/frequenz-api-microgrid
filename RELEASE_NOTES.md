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

- The following gRPC methods have been renamed:
  `StreamComponentData` -> `SubscribeComponentData`
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

- Added support for a new Component category: Relays. These are electromagnetic
  switches that control circuit breakers in the microgrid, e.g., to connect or
  disconnect an inverter from the grid. Relays support the following methods:
  - `StartComponent`
  - `StopComponent`

- Added support for a new Component category: Precharger.
  Precharging a DC (Direct Current) bus refers to a controlled process in
  electrical systems, e.g., when connecting an inverter to a battery, where the
  voltage across a DC bus is gradually increased from a low level to a desired
  level before connecting a load or initiating normal operation. This process
  is primarily used to prevent sudden surges of current that can occur when a
  load is directly connected to a high-voltage DC source.
  Precharge modules support the following methods:
  - `StartComponent`
  - `StopComponent`

- Upgraded the `frequenz-api-common` package to `v0.4.0`.

- Changed inverter DC metrics to repeated fields.

- Added fuse component. Fuses are used to protect electrical components from
  overcurrent.

- Introduced a dedicated RPC method for listing sensors in the microgrid,
  separating them from the "component" category.

- The RPC parameters have been renamed to be more consistent with the RPC names,
  and with each other.

- The package names have been changed from `frequenz.api.microgrid.<package>` to
  `frequenz.api.microgrid.v1.<package>`. `v1` is the API's major version, and
  will be incremented for breaking changes.

## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
