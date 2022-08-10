from argparse import ArgumentParser
from hello_world.version import __version__

__all__ = ["trace"]

parser = ArgumentParser(add_help=False)
optional = parser.add_argument_group("Optional arguments")
optional.add_argument(
    "-h", "--help",
    action="help",
    help="Print this help message and exit",
)
optional.add_argument(
    "-t", "--trace",
    action="store_true",
    dest="trace",
    default=False,
    help="Log package's and function's calls"
)
optional.add_argument(
    "--version",
    action="version",
    version=__version__,
    help="Print program version and exit",
)

args, unknown = parser.parse_known_args()

trace = args.trace

if __name__ == "__main__":
    parser.print_help()
