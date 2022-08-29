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


if __name__ == "__main__":
    # Compile the proto files to python files. This is done when building the
    # wheel, the source distribution (sdist) contains the *.proto files only.
    # Check the MANIFEST.in file to see which files are included in the sdist,
    # and the tool.setuptools.package-dir, tool.setuptools.package-data, and
    # tools.setuptools.packages configuration keys in pyproject.toml to see
    # which files are included in the wheel package.
    setuptools.setup(cmdclass={"build_py": BuildProto})
