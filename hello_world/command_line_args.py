from argparse import ArgumentParser
parser = ArgumentParser(add_help=False)
parser.add_argument("-t", "--trace",
                    dest="trace",
                    action="store_true",
                    default=False,
                    help="Log package's and function's calls")
args = parser.parse_args()
# parser.print_help()

trace = args.trace
