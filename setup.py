from setuptools import setup

setup(
    name="py-hello-world",
    version="0.0.5",
    packages=[
        "hello_world",
        "hello_world.util",
    ],
    entry_points={
        "console_scripts": [
            "py-hello-world     = main:say_hi",
            "py-hello-world-ni  = main_no_import:say_hi",
            "py-hello-world-sub = hello_world.main_sub:say_hi",
        ]
    }
)
