Frequenz Microgrid API
======================

Microgrid is a gRPC API used to provide monitoring and control over the
components of a microgrid.

This repository provides the core gRPC and protobuf spec together with
support for generating dedicated API packages for various languages.


Build
=====

You can use `build` to simply build the source and binary distribution:

```sh
python -m pip install build
python -m build
```

Local development
=================

You need to make sure you have the `git submodules` updated:

```sh
git submodule update --init
```

If you want to manually compile the proto files you need to install the build
dependencies manually (sadly it seems like there is no way to install build
dependencies from the `pyproject.toml` file with a simple command):

```sh
python -m pip install grpcio-tools mypy-protobuf setuptools setuptools_scm[toml] wheel
```

Then you can compile the proto files by running:

```sh
python setup.py compile_proto
```

If you have any issues with these dependencies, please check the
`pyproject.toml` file and try installing the exact supported versions instead.
