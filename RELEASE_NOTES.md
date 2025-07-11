# Frequenz Microgrid API Release Notes

## Summary

This release introduces a new preview API version, `v1alpha18`, alongside the stable `v1` API, and updates the underlying `frequenz-api-common` dependency to `v0.8.0`.

The `v1` API remains unchanged to ensure backward compatibility. All new features, including a more unified power-setting RPC and alignment with `frequenz-api-common v0.8.0`, are available exclusively in the new `v1alpha18` package.

-----

## Stable `v1` API

The `v1` API is stable and has **not** been changed in this release. Users currently on `v1` do not need to make any changes, beyond potentially updating python dependencies as described below.

The upgrade to `frequenz-api-common v0.8.0` does not affect the `v1` API, and it remains fully compatible with existing implementations.

-----

## New `v1alpha18` Preview API

A new package, `frequenz.api.microgrid.v1alpha18`, has been introduced to provide access to the latest features. The `v1alpha18` API introduces a more streamlined and robust interface compared to the stable `v1` API.

-----

## Upgrading to the `v0.18.0` release

### 1. Dependency Updates

Despite the `v1` API remaining unchanged, your project's dependencies may need to be updated, due to the following python dependency updates:

  * The minimum supported version of `protobuf` is now `6.31.1`.
  * The minimum supported version of `grpcio` is now `1.72.1`.

-----

## Upgrading to the `v1alpha18` API

Alongside upgrading to the `v0.18.0` release, you can also upgrade to the new `v1alpha18` API, which includes several significant changes and improvements.

### 1. Dependency Updates

**frequenz-api-common v0.8.0**: The `frequenz-api-common` dependency has been updated from `v0.6.1` to `v0.8.0`. The `v1alpha18` API uses the `frequenz.api.common.v1alpha8` API from the `frequenz-api-common v0.8.0` dependency, which includes several improvements and changes compared to the previous version. Please consult the release notes in `frequenz-api-common`'s for details:
  * [`v0.7.0` release notes](https://github.com/frequenz-floss/frequenz-api-common/releases/tag/v0.7.0)
  * [`v0.8.0` release notes](https://github.com/frequenz-floss/frequenz-api-common/releases/tag/v0.8.0)

-----

### 2. Removals

  * **Sensor categories**: These have been removed entirely, aligning with the underlying `frequenz-api-common v0.8.0` dependency.
  * **RPCs**: `SetComponentPowerActive` and `SetComponentPowerReactive` have been removed. Use the new `SetElectricalComponentPower` RPC instead (see below).

-----

### 3. Major Breaking Change: New Power-Setting RPC

The RPCs `SetComponentPowerActive` and `SetComponentPowerReactive` have been replaced by a single, more robust RPC: `SetElectricalComponentPower`.

  * **Unified Interface**: The new request message, `SetElectricalComponentPowerRequest`, includes a `power_type` field to specify whether you are setting `ACTIVE` or `REACTIVE` power.
  * **Streaming Response**: This RPC returns a stream of `SetElectricalComponentPowerResponse` messages, providing ongoing status updates about the power-setting operation.

-----

### 4. Symbol Renaming

Numerous symbols were renamed. The changes are primarily for clarity and consistency with the new `frequenz-api-common` API. The changes are listed below:

| Type    | Old Name                                         | New Name                                                                         |
| :------ | :----------------------------------------------- | :------------------------------------------------------------------------------- |
| RPC     | `GetMicrogridMetadata`                           | `GetMicrogrid`                                                                   |
| Message | `GetMicrogridMetadataResponse`                   | `GetMicrogridResponse`                                                           |
| RPC     | `ListComponents`                                 | `ListElectricalComponents`                                                       |
| Message | `ListComponentsRequest`                          | `ListElectricalComponentsRequest`                                                |
| Field   | `ListComponentsRequest.component_ids`            | `ListElectricalComponentsRequest.electrical_component_ids`                       |
| Field   | `ListComponentsRequest.categories`               | `ListElectricalComponentsRequest.electrical_component_categories`                |
| Message | `ListComponentsResponse`                         | `ListElectricalComponentsResponse`                                               |
| Field   | `ListComponentsResponse.components`              | `ListElectricalComponentsResponse.electrical_components`                         |
| RPC     | `ListConnections`                                | `ListElectricalComponentConnections`                                             |
| Message | `ListConnectionsRequest`                         | `ListElectricalComponentConnectionsRequest`                                      |
| Field   | `ListConnectionsRequest.starts`                  | `ListElectricalComponentConnectionsRequest.source_electrical_component_ids`      |
| Field   | `ListConnectionsRequest.ends`                    | `ListElectricalComponentConnectionsRequest.destination_electrical_component_ids` |
| Message | `ListConnectionsResponse`                        | `ListElectricalComponentConnectionsResponse`                                     |
| Field   | `ListConnectionsResponse.connections`            | `ListElectricalComponentConnectionsResponse.electrical_component_connections`    |
| RPC     | `ReceiveComponentDataStream`                     | `ReceiveElectricalComponentTelemetryStream`                                      |
| Message | `ReceiveComponentDataStreamRequest`              | `ReceiveElectricalComponentTelemetryStreamRequest`                               |
| Field   | `ReceiveComponentDataStreamRequest.component_id` | `ReceiveElectricalComponentTelemetryStreamRequest.electrical_component_ids`      |
| Message | `ReceiveComponentDataStreamResponse`             | `ReceiveElectricalComponentTelemetryStreamResponse`                              |
| Field   | `ReceiveComponentDataStreamResponse.data`        | `ReceiveElectricalComponentTelemetryStreamResponse.telemetry`                    |
| RPC     | `ReceiveSensorDataStream`                        | `ReceiveSensorTelemetryStream`                                                   |
| Message | `ReceiveSensorDataStreamRequest`                 | `ReceiveSensorTelemetryStreamRequest`                                            |
| Message | `ReceiveSensorDataStreamResponse`                | `ReceiveSensorTelemetryStreamResponse`                                           |
| Field   | `ReceiveSensorDataStreamResponse.data`           | `ReceiveSensorTelemetryStreamResponse.telemetry`                                 |
| RPC     | `AddComponentBounds`                             | `AugmentElectricalComponentBounds`                                               |
| Message | `AddComponentBoundsRequest`                      | `AugmentElectricalComponentBoundsRequest`                                        |
| Field   | `AddComponentBoundsRequest.validity_duration`    | `AugmentElectricalComponentBoundsRequest.request_lifetime`                       |
| Message | `AddComponentBoundsResponse`                     | `AugmentElectricalComponentBoundsResponse`                                       |
| Field   | `AddComponentBoundsResponse.ts`                  | `AugmentElectricalComponentBoundsResponse.valid_until_time`                      |
| RPC     | `StartComponent`                                 | `StartElectricalComponent`                                                       |
| Message | `StartComponentRequest`                          | `StartElectricalComponentRequest`                                                |
| Field   | `StartComponentRequest.component_id`             | `StartElectricalComponentRequest.electrical_component_id`                        |
| RPC     | `PutComponentInStandby`                          | `PutElectricalComponentInStandby`                                                |
| Message | `PutComponentInStandbyRequest`                   | `PutElectricalComponentInStandbyRequest`                                         |
| Field   | `PutComponentInStandbyRequest.component_id`      | `PutElectricalComponentInStandbyRequest.electrical_component_id`                 |
| RPC     | `StopComponent`                                  | `StopElectricalComponent`                                                        |
| Message | `StopComponentRequest`                           | `StopElectricalComponentRequest`                                                 |
| Field   | `StopComponentRequest.component_id`              | `StopElectricalComponentRequest.electrical_component_id`                         |
| RPC     | `AckComponentError`                              | `AckElectricalComponentError`                                                    |
| Message | `AckComponentErrorRequest`                       | `AckElectricalComponentErrorRequest`                                             |
| Field   | `AckComponentErrorRequest.component_id`          | `AckElectricalComponentErrorRequest.electrical_component_id`                     |
