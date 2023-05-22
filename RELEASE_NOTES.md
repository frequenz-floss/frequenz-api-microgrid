# Frequenz Migrogrid API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

* [Updated inverters' DC links to support hybrid and solar inverters](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/50)

  The `Inverter` message has been updated to support hybrid and solar inverters.
  The `dc` field has been renamed to `dc_battery`, and a new field `dc_solar`
  has been added.
  The `dc_battery` field is used to report the DC electricity flowing to/from
  the linked battery, and is applicable to battery and hybrid inverters.
  The `dc_solar` field is used to report the DC electricity flowing to/from the
  linked solar panels, and is applicable to solar and hybrid inverters.

## New Features

* [Added a general sensor type](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/49)

  Some sensors can be a collection of several individual sensor modules. E.g.,
  a sensor can have pyranometer and anemometer sensor modules, and report both
  irradiance and wind velocity and direction. This new sensor type
  `TYPE_GENERAL` supports such cases.

* [Added dew point to sensor metrics](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/49)

  Dew point is the temperature to which air must be cooled to become saturated
  with water vapor. When further cooled, the airborne water vapor will condense
  to form liquid water (dew).
  This metric has now been added to the `SensorMetric` enum as
  `SENSOR_METRIC_DEW_POINT`.

* [Added enum variant for setting bounds on AC reactive power](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/51)
    This will allow clients to set bounds on a component's AC reactive power.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
