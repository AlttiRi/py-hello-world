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

Or, the alternative command with less verbose output:
```bash
pip install -e .
```
`-e` for ["editable" installing](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs).

### Scripts

After installing, you can run the follow scripts in a console in any place.

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

With dependencies:
```bash
pip uninstall py-hello-world termcolor -y
```

---

### Dependencies

- [termcolor](https://pypi.org/project/termcolor/)

Manual installing:
```bash
pip install termcolor
```

Uninstalling:
```bash
pip uninstall termcolor -y
```

---

Also, it has `-h`, `--help` and `--version`:

```bash
py-hello-world -h
```
```bash
py-hello-world --help
```
```bash
py-hello-world --version
```

---

### Updating

Usually just use the same command as for installing.

To install a updated version (with changes in the repo's code), but _which still has not updated version number_, 
use [`--ignore-installed`](https://pip.pypa.io/en/latest/cli/pip_install/#options).
For example:
```bash
pip install --ignore-installed --no-deps https://github.com/AlttiRi/py-hello-world/archive/master.tar.gz
```
`--no-deps` in this case is recommended in order to do not re-install the dependecies.
