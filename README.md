# py-hello-world

It's a simple hello world example of an _installable_ Python application. 

You can install it and run in console some commands (`py-hello-world`, `py-hello-world-i`, `py-hello-world-sub`).

### Installation

_Note: [Python](https://www.python.org/downloads/) installed is required. Don't forget to check "Add to PATH" while installing._

```bash
pip install --upgrade --ignore-installed --no-deps --no-cache-dir https://github.com/AlttiRi/py-hello-world/archive/master.tar.gz
```
[[flags]](https://pip.pypa.io/en/latest/cli/pip_install/?highlight=--no-use-wheel#options)

### Dev Installation from GH
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
```bash
py-hello-world
```
```bash
py-hello-world-i
```
```bash
py-hello-world-sub
```

### UnInstallation
```bash
pip uninstall py-hello-world -y
```
