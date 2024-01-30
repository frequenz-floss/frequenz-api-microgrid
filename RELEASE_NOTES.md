# Frequenz Microgrid API Release Notes

## Summary

This release bumps the `frequenz-api-common` dependency to v0.5.3, allowing downstream projects to use a newer `frequenz-api-common` version too.

Please note that the googleapis-common-protos dependency is also bumped to v1.56.4, which is the version that api-common v0.5.4 depends on.
    
Strictly speaking, this is a breaking change, as you might need to bump your googleapis-common-protos dependency to v1.56.4 too if it is specified explicitly, but this is highly unlikely to happen and very easy to fix.
