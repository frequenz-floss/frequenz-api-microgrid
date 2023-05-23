# Frequenz Migrogrid API Release Notes

## Summary

In this release, the protobuf definitions here are being updated to use shared
definitions from [`frequenz-api-common`](https://github.com/frequenz-floss/frequenz-api-common).
The `frequenz-api-common` repository contains shared protobuf definitions that
are common to all frequenz APIs.

The `frequenz-api-microgrid` python library has also been updated to
use the [`frequenz-api-common`](https://pypi.org/project/frequenz-api-common/)
library as a dependency.

This release upgrades the minimum required python version for the library
`frequenz-api-microgrid` to 3.11.

This release also extends the API by adding new component states, and a new RPC
to set reactive power level of applicable components.

## Upgrading

* [Using `frequenz-api-common` for common proto definitions](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/57)

  The following proto definitions have been removed, and are being used from the
  `frequenz-api-common` repository instead:
  * `ComponentCategory` -> `frequenz.api.common.components.ComponentCategory`
  * `battery.Type` -> `frequenz.api.common.components.BatteryType`
  * `common.Bounds` -> `frequenz.api.common.metrics.Bounds`
  * `common.Metric` -> `frequenz.api.common.metrics.Metric`
  * `common.Ac` -> `frequenz.api.common.metrics.electrical.Ac`
  * `common.Dc` -> `frequenz.api.common.metrics.electrical.Dc`
  * `ev_charger.Type` -> `frequenz.api.common.components.EVChargerType`
  * `inverter.Type` -> `frequenz.api.common.components.InverterType`
  * `sensor.Type` -> `frequenz.api.common.components.SensorType`

  The pypi package `frequenz-api-common` is being added as a dependency to the
  python package definition, instead of generating the proto definitions using
  `protoc`. This is required, otherwise each proto library depending on
  `frequenz-api-common` will generate its own python modules for
  `frequenz-api-common`, resulting in multiple definition of the common data
  structures.

* [Upgraded minimum required python version for the python library to 3.11](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/57)

  The change to use the `frequenz-api-common` definitions forces the minimum
  required python version of the `frequenz-api-microgrid` package to be 3.11,
  as a transitive dependency inherited from the `frequenz-api-common` package.

## New Features

* [Added new battery component states](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/59)

  Three new battery component states have been added:
  * `SwitchingOn`
  * `SwitchingOff`
  * `Unknown`

* [Added a new EV charger component state](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/59)

  A new EV charger component states have been added: `Unknown`

* [Added a new inverter component state](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/59)

  A new inverter component states have been added: `Unknown`

* [Added RPC to set reactive power](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/60)

  A new RPC, named `SetPowerReactive` has been added to set reactive power for
  inverters, and other components that support it. Also, the parameters to the
  RPC can be sent using the message `SetPowerReactiveParam`.

## Bug Fixes

None
