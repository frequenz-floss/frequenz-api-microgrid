def test_package_import() -> None:
    import frequenz.api.microgrid as microgrid

    assert microgrid is not None


def test_module_import() -> None:
    import frequenz.api.microgrid.microgrid_pb2 as microgrid_pb2

    assert microgrid_pb2 is not None

    import frequenz.api.microgrid.microgrid_pb2_grpc as microgrid_pb2_grpc

    assert microgrid_pb2_grpc is not None
