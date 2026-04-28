# Frequenz Microgrid API Release Notes

## Summary

This release introduces a new preview API version, `v1alpha19`, alongside the stable `v1` API.

The `v1` API remains unchanged to ensure backward compatibility. All new features are available exclusively in the new `v1alpha19` package.

-----

## Stable `v1` API

The `v1` API is stable and has **not** been changed in this release. Users currently on `v1` do not need to make any changes, beyond potentially updating python dependencies as described below.

-----

## New `v1alpha19` Preview API

A new package, `frequenz.api.microgrid.v1alpha19`, has been introduced to provide access to the latest features. The `v1alpha19` API introduces a more streamlined and robust interface compared to the stable `v1` API.

-----

## Upgrading to the `v0.19.0` release

### 1. Dependency Updates

Despite the `v1` API remaining unchanged, your project's dependencies may need to be updated, due to the following python dependency updates:

-----

## Upgrading to the `v1alpha19` API

Alongside upgrading to the `v0.19.0` release, you can also upgrade to the new `v1alpha19` API, which includes several significant changes and improvements.

-----

### 1. Symbol Renaming

Numerous symbols were renamed. The changes are primarily for clarity and consistency with the new `frequenz-api-common` API. The changes are listed below:

| Type    | Old Name                                                                          | New Name                                                                                    |
| :------ | :-------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| Message | `ReceiveElectricalComponentTelemetryStreamRequest.ComponentTelemetryStreamFilter` | `ReceiveElectricalComponentTelemetryStreamRequest.ElectricalComponentTelemetryStreamFilter` |
