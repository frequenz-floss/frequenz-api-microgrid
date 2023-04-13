# Frequenz Migrogrid API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

<!-- Here goes notes on how to upgrade from previous versions, including if there are any deprecations and what they should be replaced with -->

## New Features

* [Added new RPC to return the microgrid metadata](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/30).
  The microgrid metadata consists of information about the overall microgrid,
  as opposed to its components, e.g., the microgrid ID, location, etc.
  This change adds a new RPC `GetMetadata()` that allows users to fetch
  microgrid metadata. The returned value is an instance of the message
  `Metadata`.

* [Added enum variants for setting bounds on currents](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/33).
  This will allow clients to set bounds on a components
  1. DC electrical current,
  2. total AC electrical current,
  3. per-phase AC electrical currents.

* [Add RPC to set active power using a signed integer](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/35).
  While reading power values, the passive sign convention is followed
  (-ve for production, and +ve for consumption). This new method allows setting
  active power values in the same convention, making the API more consistent.

* [Introduced component category-specific metadata](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/36).
  This metadata is returned in response to `ListComponents` calls,
  in a new message variable `Component.metadata`.
  This is a more general way of representing category-specific metadata,
  like category-type, and removes `Component.type`.

* [Introduced grid max-current](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/38).
  This change introduces a `grid.Metadata` message, which contains the item
  `rated_fuse_current`. This is the rating of the fuse at the grid connection
  point.
  This rating specifies the maximum amount of current, measured in amperes,
  that can flow in or out of each of the 3 phases individually.
  The current _i_ A at the grid connection point must comply with the
  following constraint: : `-rated_fuse_current <= i <= rated_fuse_current`

* [Introduced exclusion bounds](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/39).
  In the messages `common.Metric` and `common.MetricAggregation`,
  `system_bounds` has now been replaced by `system_exclusion_bounds` and
  `system_inclusion_bounds`. A metric's `value` now has to comply with the
  following constraints:

  * `value <= system_exclusion_bounds.lower` OR
    `system_exclusion_bounds.upper <= value`

  * `system_inclusion_bounds.lower <= value <= system_inclusion_bounds.upper`

  `system_inclusion_bounds` behave in the same manner as the earlier
  `system_bounds`.

  The following diagram illustrates the relationship between the exclusion and
  inclusion bounds.
  ```
    inclusion.lower                              inclusion.upper
  <-------|============|------------------|============|--------->
                 exclusion.lower    exclusion.upper
  ```
  `----` values here are disallowed and wil be rejected, and
  `====` values here are allowed and will be accepted.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
