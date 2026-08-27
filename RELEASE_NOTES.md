# Frequenz Microgrid API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

<!-- Here goes notes on how to upgrade from previous versions, including deprecations and what they should be replaced with -->

## New Features

**In both v1alpha18 and v1alpha19:**

- A new field named `bounds_token` has been added to the `AugmentElectricalComponentBoundsRequest` message. This field allows clients to specify a token that identifies their bounds contribution. If a client wants to overwrite a previously set bounds contribution, they can use the same token in a new request.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
