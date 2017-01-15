from getpass import getpass
from oslo_config import cfg
import requests

from my_dev import parser
from my_dev import ssh
from my_dev import users
from my_dev import cmd

CONF = cfg.CONF


class Base(object):
    def __init__(self, args):
        self.cmd = cmd.Cmd()
        self.command = args[0]
        self.args = args[1:]
        self.ssh()

    def ssh(self):
        user = users.Users()
        login, host = parser.parse_ssh(self.args)
        user_id = user.get_id(CONF.username)
        client = ssh.Ssh(user_id)
        # TODO(esikachev): Remove try/except when task #44 will be fixed
        try:
            client.get(host)
        except requests.exceptions.RequestException:
            password = getpass('Enter the password for ssh connection: ')
            client.create(ssh_username=login, host=host,
                          ssh_password=password)
        finally:
            ssh_get = client.get(host)
            self.cmd.ssh_cmd(ssh_username=ssh_get['ssh_username'],
                             ssh_password=ssh_get['ssh_password'],
                             host=ssh_get['host'])
