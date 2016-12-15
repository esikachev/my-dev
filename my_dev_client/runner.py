import os

import argparse


def main():
    parser = argparse.ArgumentParser(description="My-dev utility.")
    parser.add_argument('command', help="Command for running via my-dev",
                        nargs='*', default=[])
    parser.add_argument('--host', help="Host to run", nargs='?', default=None)

    args = parser.parse_args()

    command_arguments = args.command
    host_arg = args.host

    os.system(' '.join([command_arguments, host_arg]))
