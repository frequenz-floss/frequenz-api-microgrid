# License: MIT
# Copyright © 2022 Frequenz Energy-as-a-Service GmbH

"""Tests for the frequenz.api.microgrid package."""

# pylint: disable=import-outside-toplevel


def test_package_import() -> None:
    """Test if the microgrid package can be imported."""
    from frequenz.api.microgrid import v1

    assert v1 is not None


def test_module_import() -> None:
    """Test if the microgrid_pb2 package can be imported."""
    from frequenz.api.microgrid.v1 import microgrid_pb2

    assert microgrid_pb2 is not None

    from frequenz.api.microgrid.v1 import microgrid_pb2_grpc

    assert microgrid_pb2_grpc is not None
