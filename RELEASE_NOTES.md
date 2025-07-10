# Frequenz Microgrid API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

- The minimum supported version of `protobuf` was bumped to 5.28.1 and to 1.66.1 for `grpcio`. Make sure to update your dependencies accordingly.
- The `AddComponentBoundsRequest.validity_duration` field was replaced by `AddComponentBoundsRequest.request_lifetime` to match the fields in `SetComponentPowerActiveRequest` and `SetComponentPowerReactiveRequest`.
- The `AddComponentBoundsResponse.ts` field was renamed to `AddComponentBoundsResponse.valid_until` for extra clarity and also to match the fields in `SetComponentPowerActiveResponse` and `SetComponentPowerReactiveResponse`.
- The version of `frequenz-api-common` has been updated from v0.6.1 to to v0.8.0. Please refer to the release notes for `frequenz-api-common` versions [v0.7.0](https://github.com/frequenz-floss/frequenz-api-common/releases/tag/v0.8.0) and [v0.8.0](https://github.com/frequenz-floss/frequenz-api-common/releases/tag/v0.8.0) and update your code accordingly. The following changes have been made in the Microgrid API to align with the changes in `frequenz-api-common`:
  - Sensor categories have been removed from `frequenz-api-common`, and are therefore removed from the Microgrid API as well.
  - `component` and `Component` have been renamed to `electrical_component` and `ElectricalComponent`, respectively. This is keep in line with the naming conventions used in `frequenz-api-common`.
  - `ListComponentConnectionsResponse.connections` has been renamed to `ListElectricalComponentConnectionsResponse.electrical_component_connections` to match the naming conventions used in `frequenz-api-common`.
  - `ReceiveComponentDataStreamResponse.data` has been renamed to `ReceiveElectricalComponentDataStreamResponse.telemetry` to match the naming conventions used in `frequenz-api-common`.
  - `ReceiveSensorDataStreamResponse.data` has been renamed to `ReceiveSensorDataStreamResponse.telemetry` to match the naming conventions used in `frequenz-api-common`.
  - `ReceiveElectricalComponentDataStream` RPC method has been renamed to `ReceiveElectricalComponentTelemetryStream` to match the naming conventions used in `frequenz-api-common`.
  - `ReceiveElectricalComponentDataStreamRequest` RPC method has been renamed to `ReceiveElectricalComponentTelemetryStreamRequest` to match the naming conventions used in `frequenz-api-common`.
  - `ReceiveElectricalComponentDataStreamResponse` RPC method has been renamed to `ReceiveElectricalComponentTelemetryStreamResponse` to match the naming conventions used in `frequenz-api-common`.
  - `ReceiveSensorDataStream` RPC method has been renamed to `ReceiveSensorTelemetryStream` to match the naming conventions used in `frequenz-api-common`.
  - `ReceiveSensorDataStreamRequest` RPC method has been renamed to `ReceiveSensorTelemetryStreamRequest` to match the naming conventions used in `frequenz-api-common`.
  - `ReceiveSensorDataStreamResponse` RPC method has been renamed to `ReceiveSensorTelemetryStreamResponse` to match the naming conventions used in `frequenz-api-common`.
  - `ListComponentConnectionRequests.starts` has been renamed to `ListElectricalComponentConnectionRequests.source_electrical_component_ids` to match the naming conventions used in `frequenz-api-common`.
  - `ListComponentConnectionRequests.ends` has been renamed to `ListElectricalComponentConnectionRequests.destination_electrical_component_ids` to match the naming conventions used in `frequenz-api-common`.
- The RPC `GetMicrogridMetadata` has been renamed to `GetMicrogrid` to better align with the naming convention in `frequenz-api-common`.
- The `GetMicrogridMetadataResponse` message has been renamed to `GetMicrogridResponse` to better align with the naming convention in `frequenz-api-common`.
- The response messages for the `SetElectricalComponentPowerActive` and
`SetElectricalComponentPowerReactive` RPCs have been changed to return a stream of responses instead of a single response. This allows the server to provide ongoing status updates for the request, which is useful when the electrical component cannot immediately set its output power to the requested value.
- The RPC `AddComponentBounds` has been renamed to `AugmentElectricalComponentBounds`.
- `SetElectricalComponentPowerActive` and `SetElectricalComponentPowerReactive` RPCs ave been replaced by a new RPC `SetElectricalComponentPower`. The new RPC allows setting either the active or reactive power of an electrical component, depending on the value of the `power_type` field in the request message.

## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
