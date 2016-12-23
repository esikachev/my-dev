import os

import argparse
from getpass import getpass

from my_dev import 


def main():
    parser = argparse.ArgumentParser(description="My-dev utility.")
    parser.add_argument('command', help="Command for running via my-dev",
                        nargs='*', default=[])
    parser.add_argument('init', default=False, action='store_true',
                        help="Init basic config")
    parser.add_argument('--username', '-u', default=None, nargs='?',
                        help='Specify username')
    parser.add_argument('--email', '-e', default=None, nargs='?',
                        help='Specify e-mail')
     
    args = parser.parse_args()

    command_arguments = args.command
    init = args.init

    if init:
        username = raw_input("Insert the username: ")
        email = raw_input("Insert the e-mail: ")

