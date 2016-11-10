import os

import argparse


def main():
    parser = argparse.ArgumentParser(description="My-dev utility.")
    parser.add_argument('command', help="Command for running via my-dev",
                        nargs='*', default=[])

    args = parser.parse_args()

    command_arguments = args.command

    os.system(' '.join(command_arguments))
