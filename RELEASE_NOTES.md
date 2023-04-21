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

  Two new simple RPCs for setting exclusion and inclusion bounds have been
  added:
  * `AddExclusionBounds`: adds a pair of exclusion bounds for a given component
    and metric, and returns the UTC timestamp until when it will stay in effect.
  * `AddInclusionBounds`: adds a pair of inclusion bounds for a given component
    and metric, and returns the UTC timestamp until when it will stay in effect.

  Exclusion bounds are a useful tool for enhancing the performance of a system.
  They can be used to restrict the acceptance of commands that fall below a
  certain threshold, which can help ensure the smooth functioning of the system.
  E.g., exclusion bounds can be set to limit the minimum charging power to a
  sufficiently high level, preventing a peak-shaver client from sending charge
  powers that are too low when a DC heater client is executing a charge pulse.
  This can significantly improve the overall performance of the DC heating
  mechanism.

  The RPC `SetBounds` has been deprecated.

* [Removed deprecated code](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/44)
  The following deprecated code has been removed:
  * The `COMPONENT_CATEGORY_LOAD` variant from the `ComponentCategory` enum.
  * The `COMPONENT_CATEGORY_JUNCTION` variant from the `ComponentCategory` enum.
  * The RPCs `Charge` and `Discharge`, in favour of RPC `SetPowerActive`.
  * The RPC `SetBounds`, in favour of RPCs `AddExclusiveBounds` and
    `AddInclusiveBounds`.

  This removal also includes code that has been deprecated after the last major
  release. The reason to remove these deprecations now is to have a leaner API
  earlier, since we are already on the way for a major release now.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
