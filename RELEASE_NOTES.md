# Frequenz Migrogrid API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

* [Upgraded `frequenz-api-common` to v0.3.0](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/65)

  The submodule `frequenz-api-common` has been upgraded to v0.3.0.
  This version renames the enum representing EV charger types to `EvChargerType`
  and defined the `MetricAggregation` message, which was previously defined in
  `frequenz-api-microgrid`.

  Since the message `MetricAggregation` is now being imported from the common
  specs, it has been removed from the file `common.proto`.

* [Renamed message `EVCharger` to `EvCharger`](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/65)

  This is done to use same naming convention as `frequenz-api-common`.
  Note that a similar renaming was done in `frequenz-api-common` v0.3.0 to
  improve the code quality of the derived rust code using prost.


## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
