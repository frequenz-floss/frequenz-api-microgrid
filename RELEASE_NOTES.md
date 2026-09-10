# Frequenz Microgrid API Release Notes

## Summary

This release adds a new RPC to clear previously set bounds contributions for electrical components, and introduces a new field to the `AugmentElectricalComponentBoundsRequest` message to allow clients to specify a token for their bounds contribution.

## New Features

**In both v1alpha18 and v1alpha19:**

- A new field named `bounds_token` has been added to the `AugmentElectricalComponentBoundsRequest` message. This field allows clients to specify a token that identifies their bounds contribution. If a client wants to overwrite a previously set bounds contribution, they can use the same token in a new request.
- A new RPC named `ClearElectricalComponentBounds` has been introduced. This RPC allows clients to withdraw a previously set bounds contribution by specifying the component, metric, and the token associated with that contribution.
