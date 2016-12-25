import os
from getpass import getpass

import argparse
from oslo_config import cfg

from my_dev import config
from my_dev import users
from my_dev import utils

CONF = cfg.CONF


def main():
    parser = argparse.ArgumentParser(description="My-dev utility.")
    parser.add_argument('command', help="Command for running via my-dev",
                        nargs='*', default=[])
    parser.add_argument('init', default=False, action='store_true',
                        help="Init basic config")
    parser.add_argument('--username', '-u', default=None, nargs='?',
                        help='Specify username')
    parser.add_argument('--password', '-p', default=None, nargs='?',
                        help='Specify password')
    parser.add_argument('--email', '-e', default=None, nargs='?',
                        help='Specify e-mail')
     
    args = parser.parse_args()

    command_arguments = args.command
    init = args.init
    username = args.username
    email = args.email
    password = args.password

    if init:
        username = username if username else raw_input("Insert the username: ")
        password = password if password else getpass()
        email = email if email else raw_input("Insert the e-mail: ")

        user = users.Users()
        user.create(username, password, email)
       
        utils.write_to_config(username, CONF.host)
