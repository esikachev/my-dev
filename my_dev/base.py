from getpass import getpass
from oslo_config import cfg

from my_dev import cmd
from my_dev import parser
from my_dev import ssh
from my_dev import users

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
        if client.get(host).get('status_code') == 404:
            password = self.enter_pass('Enter the password for ssh '
                                       'connection: ')
            alias = raw_input('Would you like to use alias for this '
                              'connection?: ')
            client.create(ssh_username=login, host=host,
                          ssh_password=password, alias=alias)
        ssh_get = client.get(host)
        self.cmd.ssh_cmd(ssh_username=ssh_get['ssh_username'],
                         ssh_password=ssh_get['ssh_password'],
                         host=ssh_get['host'])

    def enter_pass(self, message):
        return getpass(message)
