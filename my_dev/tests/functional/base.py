
import sys

import testtools

from my_dev.tests.functional import utils
from my_dev import users
from my_dev import runner
from my_dev import ssh


class TestBase(testtools.TestCase):
    def setUp(self):
        super(TestBase, self).setUp()
        self.user = users.Users()

    def create_user(self, username=None, password=None, email=None):
        username = username if username else utils.rand_name('username')
        password = password if password else utils.rand_name('password')
        email = email if email else utils.rand_name('email')
        return self.user.create(username, password, email)

    def create_ssh(self, user_id, ssh_username=utils.rand_name('username'),
                   ssh_password=utils.rand_name('password'),
                   host=utils.rand_name('host'),
                   alias=utils.rand_name('alias')):
        ssh = ssh.Ssh(user_id)
        return ssh.create(host=host, ssh_username=ssh_username,
                          ssh_password=ssh_password, alias=alias)
