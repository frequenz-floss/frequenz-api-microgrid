# Frequenz Migrogrid API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

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

## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
