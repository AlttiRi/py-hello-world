#!/usr/bin/env python
from hello_world.command_line_args import trace


def say_hi():
    if trace:
        print("[trace]: main.py:say_hi()")
    print("Hello World!")


if __name__ == "__main__":
    say_hi()
