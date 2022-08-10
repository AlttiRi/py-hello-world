from setuptools import setup  # find_packages
from hello_world.version import __version__

setup(
    name="py-hello-world",
    version=__version__,
    packages=[
        "hello_world",
        "hello_world.sub",
    ],  # find_packages(),
    install_requires=[
        "termcolor>=1.1.0",
    ],
    entry_points={
        "console_scripts": [
            "py-hello-world     = hello_world.__main__:say_hi",
            "py-hello-world-wi  = hello_world.__main__with_import:say_hi",
            "py-hello-world-sub = hello_world.sub.__main__sub:say_hi",
        ]
    }
)
