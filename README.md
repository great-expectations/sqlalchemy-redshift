# gx-sqlalchemy-redshift

This is a fork of the
`sqlalchemy-redshift <https://github.com/sqlalchemy-redshift/sqlalchemy-redshift>`_
project that is installable with sqlalchemy 2 and usable with `Great Expectations <https://github.com/great-expectations/great_expectations>`_.
It is **NOT** a fully working sqlalchemy dialect. In particular, the dialect does not support the `get_columns` method.

## Local setup

```sh
python --version; # confirm python >3.10
python -m venv .venv; # create a virtual env
source .venv/bin/activate;
pip install --upgrade pip # pip 25.0.1
pip install tox; # tox 4.25.0
tox --notest -e lint # run the linter
```

## Release

Prerequisite: accounts on both TestPyPI and production PyPI repos.

```sh
touch .pypirc
```

Then add this contents to `.pypirc`:

```
[pypi]
  username = __token__
  password = YOUR_API_TOKEN

[testpypi]
  username = __token__
  password = YOUR_API_TOKEN
```

First, create a build and upload the build to TestPyPI:

```sh
python -m venv .venvtestpypi; # create a build env
source .venvtestpypi/bin/activate;
pip install --upgrade build twine; # Install build tools: build 1.2.2.post1, twine 6.1.0
python -m build; # Create source distribution and wheel
twine check dist/*; # Check the distribution
twine upload --repository testpypi dist/*; # Upload to TestPyPI
pip install --index-url https://test.pypi.org/simple/ gx-sqlalchemy-redshift; # test download
twine upload dist/*; # Upload to production PyPI
pip install gx-sqlalchemy-redshift; # test download
```

Then, test install in an isolated venv (as if you were a user and not a maintainer):

```sh
python -m venv .venvtestinstall; # create a test env
source .venvtestinstall/bin/activate;
pip install gx-sqlalchemy-redshift;
pip list;
pip show gx-sqlalchemy-redshift;
```
