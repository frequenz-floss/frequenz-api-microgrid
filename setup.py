"""Build script for the frequenz-api-microgrid python package.

Copyright © 2022 Frequenz Energy-as-a-Service GmbH.
"""

import pathlib
import sys
import subprocess

import setuptools
import setuptools.command.build_py


class CompileProto(setuptools.Command):
    """Command class to build the Python protobuf files."""

    description = "compile protobuf files in proto/"
    user_options = []

    def initialize_options(self):
        """Initialize options."""

    def finalize_options(self):
        """Finalize options."""

    def run(self):
        """Compile the Python protobuf files."""
        proto_files = [str(p) for p in pathlib.Path("proto").rglob("*.proto")]
        protoc_cmd = (
            [sys.executable]
            + """-m grpc_tools.protoc
                    -I proto
                    -I submodules/api-common-protos
                    --python_out=py
                    --grpc_python_out=py
                    --mypy_out=py
                    --mypy_grpc_out=py
                    """.split()
            + proto_files
        )
        print(f"Compiling proto files via: {' '.join(protoc_cmd)}")
        subprocess.run(protoc_cmd, check=True)


class BuildPy(setuptools.command.build_py.build_py, CompileProto):
    """Command class to build the Python protobuf files."""

    def run(self):
        """Compile the Python protobuf files and run regular `build_py`."""
        CompileProto.run(self)
        setuptools.command.build_py.build_py.run(self)


if __name__ == "__main__":
    setuptools.setup(
        cmdclass={
            "compile_proto": CompileProto,
            # Compile the proto files to python files. This is done when building
            # the wheel, the source distribution (sdist) contains the *.proto files
            # only. Check the MANIFEST.in file to see which files are included in
            # the sdist, and the tool.setuptools.package-dir,
            # tool.setuptools.package-data, and tools.setuptools.packages
            # configuration keys in pyproject.toml to see which files are included
            # in the wheel package.
            "build_py": BuildPy,
        }
    )
