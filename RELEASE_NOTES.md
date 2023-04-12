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

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
