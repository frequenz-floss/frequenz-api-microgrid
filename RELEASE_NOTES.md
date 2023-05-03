# Frequenz Migrogrid API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

<!-- Here goes notes on how to upgrade from previous versions, including if there are any deprecations and what they should be replaced with -->

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

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
