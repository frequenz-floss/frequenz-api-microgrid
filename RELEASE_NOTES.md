# Frequenz Microgrid API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

- This release upgrades `frequenz-api-common` to version `v0.6.0`. Please refer
  to the [release notes](https://github.com/frequenz-floss/frequenz-api-common/releases/tag/v0.6.0)
  of `frequenz-api-common` for more information.

- A new RPC named `AddComponentBounds` has been introduced, which accepts only
  inclusive bounds. The old RPCs `AddComponentInclusionBounds` and
  `AddComponentExclusionBounds` have been removed.

- The enum `ComponentBoundsTargetMetric` has been removed in favour of the
  `Metric` enum from `frequenz-api-common`.

## New Features

- The `AddComponentBoundsRequest` message has a field `validity_duration` which
  allows the user to specify the duration for which the bounds are valid. The
  bounds will be automatically removed after the specified duration. The client
  can select between 5 seconds, 1 minute, 5 minutes, and 15 minutes. If set to
  `UNSPECIFIED`, the bounds will be valid for a default duration of 5 seconds.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
