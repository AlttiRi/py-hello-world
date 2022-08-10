from argparse import ArgumentParser

__all__ = ["trace"]

parser = ArgumentParser(add_help=False)
parser.add_argument("-h", "--help",
                    action="help",
                    help="Print this help message and exit")
parser.add_argument("-t", "--trace",
                    action="store_true",
                    dest="trace",
                    default=False,
                    help="Log package's and function's calls")
args = parser.parse_args()

trace = args.trace

if __name__ == "__main__":
    parser.print_help()
