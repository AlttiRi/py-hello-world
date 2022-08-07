from setuptools import setup  # find_packages

setup(
    name="py-hello-world",
    version="0.1.1",
    packages=[
        "hello_world",
        "hello_world.sub",
    ],  # find_packages(),
    entry_points={
        "console_scripts": [
            "py-hello-world     = hello_world.main:say_hi",
            "py-hello-world-wi  = hello_world.main_with_import:say_hi",
            "py-hello-world-sub = hello_world.sub.main_sub:say_hi",
        ]
    }
)
