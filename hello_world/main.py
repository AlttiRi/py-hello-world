#!/usr/bin/env python
from util.get_text import get_text


def say_hi():
    print("[main.py]:", get_text())


if __name__ == "__main__":
    say_hi()