# License: MIT
# Copyright © 2022 Frequenz Energy-as-a-Service GmbH

"""Tests for the frequenz.api.microgrid package."""


def test_package_import() -> None:
    """Test that the package can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.microgrid import v1

    assert v1 is not None


def test_module_import_components() -> None:
    """Test that the modules can be imported."""
    # pylint: disable=import-outside-toplevel
    from frequenz.api.microgrid.v1 import microgrid_pb2

    assert microgrid_pb2 is not None

    # pylint: disable=import-outside-toplevel
    from frequenz.api.microgrid.v1 import microgrid_pb2_grpc

    assert microgrid_pb2_grpc is not None
