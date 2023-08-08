# License: MIT
# Copyright © 2022 Frequenz Energy-as-a-Service GmbH

"""Tests for the frequenz.api.microgrid package."""

def test_package_import() -> None:
    """Test if the microgrid package can be imported."""
    import frequenz.api.microgrid as microgrid

    assert microgrid is not None


def test_module_import() -> None:
    """Test if the microgrid_pb2 package can be imported."""
    import frequenz.api.microgrid.microgrid_pb2 as microgrid_pb2

    assert microgrid_pb2 is not None

    import frequenz.api.microgrid.microgrid_pb2_grpc as microgrid_pb2_grpc

    assert microgrid_pb2_grpc is not None
