# py-hello-world

It's a simple hello world example of an **_installable_** command line Python application.

You can install it and run in console some commands (`py-hello-world`, `py-hello-world-i`, `py-hello-world-sub`).

Also, it has optional command line argument `-t`/`--trace`. 
With it the program logs package's and function's calls.
It almost makes no sense, but it's only just an example usage of command line arguments.


### Installation


_Note: [Python](https://www.python.org/downloads/) installed is required. Don't forget to check "Add to PATH" while installing._

```bash
pip install https://github.com/AlttiRi/py-hello-world/archive/master.tar.gz
```

_Or_, if you have also [Git](https://git-scm.com/downloads) installed:

```bash
pip install git+https://github.com/AlttiRi/py-hello-world.git
```

_Or_, a more complex example (check the [flags](https://pip.pypa.io/en/latest/cli/pip_install/?highlight=--no-use-wheel#options)):

```bash
pip install --upgrade --ignore-installed --no-deps --no-cache-dir https://github.com/AlttiRi/py-hello-world/archive/master.tar.gz
```


### Dev Installation (from GH)
```bash
git clone https://github.com/AlttiRi/py-hello-world.git
cd py-hello-world
python setup.py develop
```

### Dev Installation (local)
```bash
python setup.py develop
```

### Scripts

After installing you can run the follow scripts in a console in any place.

```bash
py-hello-world
```
```bash
py-hello-world-wi
```
```bash
py-hello-world-sub
```

The same, but with `-t`, `--trace` command line argument:
```bash
py-hello-world -t
```
```bash
py-hello-world-wi --trace
```
```bash
py-hello-world-sub --trace
```

### UnInstallation
```bash
pip uninstall py-hello-world -y
```
