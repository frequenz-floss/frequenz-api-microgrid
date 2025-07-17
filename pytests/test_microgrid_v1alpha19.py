# License: MIT
# Copyright © 2022 Frequenz Energy-as-a-Service GmbH

"""Tests for the frequenz.api.microgrid package."""

import pytest


def test_package_import() -> None:
    """Test that the package can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.microgrid import v1alpha19

    assert v1alpha19 is not None


@pytest.mark.filterwarnings(
    r"ignore:.*Protobuf gencode version .* is exactly one major version older "
    "than the runtime version.*:UserWarning"
)
def test_package_import_microgrid() -> None:
    """Test that the package can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.microgrid.v1alpha19 import microgrid_pb2

    assert microgrid_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.microgrid.v1alpha19 import microgrid_pb2_grpc

    assert microgrid_pb2_grpc is not None
