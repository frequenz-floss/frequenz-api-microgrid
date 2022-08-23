"""Build script for the frequenz-api-microgrid python package.

Copyright © 2022 Frequenz Energy-as-a-Service GmbH.
"""

import sys
import subprocess

import setuptools
from setuptools.command.build_py import build_py


class BuildProto(build_py):
    """Command class to build the Python protobuf files."""

    def run(self):
        """Build the Python protobuf files and run regular `build_py`."""
        subprocess.check_call(["./build-py-proto", sys.executable], shell=True)
        build_py.run(self)


setuptools.setup(
    name="frequenz-api-microgrid",
    author="Frequenz Energy-as-a-Service GmbH",
    description="Frequenz gRPC API for monitoring and control of microgrids",
    use_scm_version={"version_scheme": "post-release"},
    cmdclass={"build_py": BuildProto},
    install_requires=[
        "googleapis-common-protos >= 1.56.2, < 2",
        "grpcio >= 1.47.0, < 2",
    ],
    license="MIT",
    package_dir={"": "py"},
    package_data={
        "frequenz.api.microgrid": [
            "py.typed",
            "*.pyi",
        ],
    },
    packages=setuptools.find_namespace_packages(where="py"),
    python_requires=">= 3.7, < 4",
)
