# Frequenz Migrogrid API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

<!-- Here goes notes on how to upgrade from previous versions, including if there are any depractions and what they should be replaced with --> 

## New Features

* [Added new RPC to return the microgrid metadata](https://github.com/frequenz-floss/frequenz-api-microgrid/pull/30).
  The microgrid metadata consists of information about the overall microgrid,
  as opposed to its components, e.g., the microgrid ID, location, etc.
  This change adds a new RPC `GetMetadata()` that allows users to fetch
  microgrid metadata. The returned value is an instance of the message
  `Metadata`.

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
