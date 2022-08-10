from termcolor import colored

from hello_world.command_line_args import trace
from hello_world.sub.util import get_text


def say_hi():
    if trace:
        print("[trace]: sub.__main__sub.py:say_hi()")
    print(colored(get_text(), color="magenta", attrs=["bold"]))


if __name__ == "__main__":
    say_hi()
