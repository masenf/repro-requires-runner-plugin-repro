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

# Results

## tox 4.2.8

```
ROOT: 71 D setup logging to DEBUG on pid 12802 [tox/report.py:221]
ROOT: 99 W will run in automatically provisioned tox, host /Users/masen/code/tox-dev/venv/tox-upstream/bin/python3.11 is missing [requires (has)]: tox-example-plugin [tox/provision.py:124]
Traceback (most recent call last):
  File "/Users/masen/code/tox-dev/minimal-plugin2/../venv/tox-upstream/bin/tox", line 8, in <module>
    sys.exit(run())
             ^^^^^
  File "/Users/masen/code/tox-dev/venv/tox-upstream/lib/python3.11/site-packages/tox/run.py", line 19, in run
    result = main(sys.argv[1:] if args is None else args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/masen/code/tox-dev/venv/tox-upstream/lib/python3.11/site-packages/tox/run.py", line 41, in main
    result = provision(state)
             ^^^^^^^^^^^^^^^^
  File "/Users/masen/code/tox-dev/venv/tox-upstream/lib/python3.11/site-packages/tox/provision.py", line 125, in provision
    return run_provision(provision_tox_env, state)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/masen/code/tox-dev/venv/tox-upstream/lib/python3.11/site-packages/tox/provision.py", line 143, in run_provision
    tox_env: PythonRun = cast(PythonRun, state.envs[name])
                                         ~~~~~~~~~~^^^^^^
  File "/Users/masen/code/tox-dev/venv/tox-upstream/lib/python3.11/site-packages/tox/session/env_select.py", line 336, in __getitem__
    return self._defined_envs[item].env
           ^^^^^^^^^^^^^^^^^^
  File "/Users/masen/code/tox-dev/venv/tox-upstream/lib/python3.11/site-packages/tox/session/env_select.py", line 192, in _defined_envs
    run_env = self._build_run_env(name)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/masen/code/tox-dev/venv/tox-upstream/lib/python3.11/site-packages/tox/session/env_select.py", line 251, in _build_run_env
    runner = REGISTER.runner(cast(str, env_conf["runner"]))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/masen/code/tox-dev/venv/tox-upstream/lib/python3.11/site-packages/tox/tox_env/register.py", line 72, in runner
    return self._run_envs[name]
           ~~~~~~~~~~~~~~^^^^^^
KeyError: 'example'
tox --version
4.2.8 from /Users/masen/code/tox-dev/venv/tox-upstream/lib/python3.11/site-packages/tox/__init__.py
```
