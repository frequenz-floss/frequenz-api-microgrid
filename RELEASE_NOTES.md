# Frequenz Microgrid API Release Notes

## Summary

This release introduces a new preview API version, `v1alpha19`, alongside the stable `v1` API.

The `v1` API remains unchanged to ensure backward compatibility. All new features are available exclusively in the new `v1alpha19` package.

-----

## Stable `v1` API

The `v1` API is stable and has **not** been changed in this release. Users currently on `v1` do not need to make any changes, beyond potentially updating python dependencies as described below.

## Stable `v1alpha18` Preview API

The previous preview version, `v1alpha18`, is stable. It has the following symbol additions as compared to the `v1.18.0` release:

| Type    | Name                                                                               |
| :------ | :--------------------------------------------------------------------------------- |
| Enum    | `frequenz.api.microgrid.v1alpha18.PowerSource`                                     |
| Field   | `frequenz.api.microgrid.v1alpha18.SetElectricalComponentPowerRequest.power_source` |

-----

## New `v1alpha19` Preview API

A new package, `frequenz.api.microgrid.v1alpha19`, has been introduced to provide access to the latest features. The `v1alpha19` API introduces a more streamlined and robust interface compared to the stable `v1` API. It builds on top of `v1alpha18` and incorporates all of its additions, including those listed in the [Stable `v1alpha18` Preview API](#stable-v1alpha18-preview-api) section above.

-----

## Upgrading to the `v0.19.0` release

### 1. Dependency Updates

Despite the `v1` or `v1alpha18` APIs remaining backward-compatible, your project's dependencies may need to be updated, due to python dependency updates.

-----

## Upgrading to the `v1alpha19` API

Alongside upgrading to the `v0.19.0` release, you can also upgrade to the new `v1alpha19` API, which includes several changes and improvements over the `v1` and `v1alpha18` packages.

-----

### 1. Symbol Renaming

Numerous symbols were renamed. The changes are primarily for clarity and consistency with the new `frequenz-api-common` API. The changes are listed below:

| Type    | Old Name                                                                          | New Name                                                                                    |
| :------ | :-------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| Message | `ReceiveElectricalComponentTelemetryStreamRequest.ComponentTelemetryStreamFilter` | `ReceiveElectricalComponentTelemetryStreamRequest.ElectricalComponentTelemetryStreamFilter` |
