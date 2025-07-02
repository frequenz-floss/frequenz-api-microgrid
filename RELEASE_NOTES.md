# Frequenz Microgrid API Release Notes

## Summary

<!-- Here goes a general summary of what this release is about -->

## Upgrading

- The minimum supported version of `protobuf` was bumped to 5.28.1 and to 1.66.1 for `grpcio`. Make sure to update your dependencies accordingly.
- The `AddComponentBoundsRequest.validity_duration` field was replaced by `AddComponentBoundsRequest.request_lifetime` to match the fields in `SetComponentPowerActiveRequest` and `SetComponentPowerReactiveRequest`. The default value was also changed from 5 to 60 seconds.
- The `AddComponentBoundsResponse.ts` field was renamed to `AddComponentBoundsResponse.valid_until` for extra clarity and also to match the fields in `SetComponentPowerActiveResponse` and `SetComponentPowerReactiveResponse`.
- The version of `frequenz-api-common` has been updated to v0.7.0. Please refer to the [release notes](https://github.com/frequenz-floss/frequenz-api-common/releases/tag/v0.7.0) and update your code accordingly.
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

## New Features

<!-- Here goes the main new features and examples or instructions on how to use them -->

## Bug Fixes

<!-- Here goes notable bug fixes that are worth a special mention or explanation -->
