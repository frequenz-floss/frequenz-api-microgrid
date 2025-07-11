# Frequenz Microgrid API Release Notes

## Summary

This release introduces significant **breaking changes** to align with the `frequenz-api-common v0.8.0` release. Key updates include a more unified power-setting RPC, numerous symbol renames for consistency, and updated dependency requirements.

-----

## Upgrading

### 1. Dependency Updates

Your project's dependencies may need to be updated.

  * The minimum supported version of `protobuf` is now **`6.31.1`**.
  * The minimum supported version of `grpcio` is now **`1.72.1`**.
  * The `frequenz-api-common` dependency has been updated from `v0.6.1` to **`v0.8.0`**. Please consult the common API's release notes for details:
      * [`v0.7.0` release notes](https://github.com/frequenz-floss/frequenz-api-common/releases/tag/v0.7.0)
      * [`v0.8.0` release notes](https://github.com/frequenz-floss/frequenz-api-common/releases/tag/v0.8.0)

-----

### 2. Removals

  * **Sensor categories**: These have been removed entirely, aligning with the underlying `frequenz-api-common` dependency.
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
