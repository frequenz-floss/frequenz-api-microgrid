Contributing to Frequenz Microgrid API
======================================


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


Releasing
=========

These are the steps to create a new release:

1. Get the latest head you want to create a release from.

1. Update the `RELEASE_NOTES.md` file if it is not complete, up to date, and
   clean from template comments (`<!-- ... ->`) and empty sections. Submit
   a pull request if an update is needed, wait until it is merged, and update
   the latest head you want to create a release from to get the new merged pull
   request.

3. Create a new signed tag using the release notes and
   a [semver](https://semver.org/) compatible version number with a `v` prefix,
   for example:

   ```sh
   git tag -s -F RELEASE_NOTES.md v0.0.1
   ```

4. Push the new tag.

5. A GitHub action will test the tag and if all goes well it will create
   a [GitHub
   Release](https://github.com/frequenz-floss/frequenz-api-microgrid/releases),
   create a new
   [announcement](https://github.com/frequenz-floss/frequenz-api-microgrid/discussions/categories/announcements)
   about the release, and upload a new package to
   [PyPI](https://pypi.org/project/frequenz-api-microgrid/) automatically.

6. Once this is done, reset the `RELEASE_NOTES.md` with the template:

   ```sh
   cp .github/RELEASE_NOTES.template.md RELEASE_NOTES.md
   ```

   Commit the new release notes and create a PR (this step should be automated
   eventually too).

7. Celebrate!
