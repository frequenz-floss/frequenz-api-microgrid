# Frequenz Microgrid API Release Notes

## Summary

This release updates the `frequenz-api-common` submodule from v0.8.4 to v0.8.13, and adds the `v1alpha20` preview, in which the service manages the power of pools of electrical components and streams telemetry aggregated over several components.

## Upgrading

The minimum `frequenz-api-common` version is now 0.8.13, which has the types the `v1alpha20` package uses.

## New Features

The `frequenz-api-common` submodule has been updated from v0.8.4 to v0.8.13. See the release notes for that submodule here: https://github.com/frequenz-floss/frequenz-api-common/releases

The new `v1alpha20` package has every RPC of `v1alpha19`, and these new ones:

- `ProposePoolPower` proposes a power, bounds, or both, for a pool of electrical components, or withdraws a pool's proposal. The service arbitrates the proposals of all pools by priority and sets the components' power itself. A proposal stays in effect for its request lifetime, 60 seconds by default, and the client renews it by sending it again.
- `ReceivePoolPowerReportStream` streams reports on a pool's components, as seen from a priority, each a `PoolPowerReport` from `frequenz-api-common`: the target power, the power the components are set to now and when they are expected to reach the target, the power the proposals at that priority got, the bounds still available to them, the power of components that can't be controlled, and, if the client asks for them, each component's setpoint and outcome.
- `ReceiveAggregatedTelemetryStream` streams a value computed from the telemetry of several components and resampled by the service, for example the active power of a set of batteries. The value is an `AggregateExpression` from `frequenz-api-common`: aggregates the service computes from the component graph, single metrics of single components, formulas and constants, combined with sum, difference, scale, min, max and coalesce. The request can set the resampling interval and the `ResamplingFunction`.

The pool RPCs are defined for batteries and active power first. `power_type` is there for reactive power, which isn't supported yet.
