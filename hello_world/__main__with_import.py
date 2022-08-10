#!/usr/bin/env python
from termcolor import colored

from hello_world.command_line_args import trace
from hello_world.sub.util import get_text


def say_hi():
    if trace:
        print("[trace]: __main__with_import.py:say_hi()")
    text = get_text()
    print(colored(text, color="cyan", attrs=["bold"]))


if __name__ == "__main__":
    say_hi()
