from setuptools import setup  # find_packages

setup(
    name="py-hello-world",
    version="0.0.12",
    packages=[
        "hello_world",
        "hello_world.util",
    ],  # find_packages(),
    entry_points={
        "console_scripts": [
            "py-hello-world     = hello_world.main:say_hi",
            "py-hello-world-i   = hello_world.main_import:say_hi",
            "py-hello-world-sub = hello_world.util.main_sub:say_hi",
        ]
    },
    package_data={"": ["readme.md"]},
)
