#!/usr/bin/env python
from termcolor import colored

from hello_world.command_line_args import trace


def say_hi():
    if trace:
        print("[trace]: __main__.py:say_hi()")
    print(colored("Hello World! 123", color="green", attrs=["bold"]))


if __name__ == "__main__":
    say_hi()
