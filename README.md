# "minimal" example

Any environments referencing an unknown `runner` key will raise an exception.

If a plugin registers a new `runner` type, then it can be used in `tox.ini`.

However, if the `tox.ini` relies on `requires` to provision plugins that
provide the new runner type, provisioning should NOT fail on unknown runner
keys, since they may be provided by the environment being provisioned.

## 1. build plugin and fake local index

tox -c example-plugin

## 2. Point to the fake local index

export PIP_INDEX_URL=file://$(realpath $(pwd)/example-plugin/.tox/index/simple)
export PIP_EXTRA_INDEX_URL=https://pypi.org/simple/

## 3. run tox in the root

tox -vv
