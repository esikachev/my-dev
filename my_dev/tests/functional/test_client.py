import sys

import testtools

from my_dev import runner
from my_dev import ssh
from my_dev.tests.functional import base
from my_dev.tests.functional import utils
from my_dev import users


class TestClient(base.TestBase):
    def test_client(self):
        user = self.create_user()
        user_by_id = self.user.get(user['id'])
        user_by_name = self.user.get(user['username'])
        self.assertEqual(user_by_id, user_by_name)
        self.user.delete(user['id'])

    def test_create_already_existed_user(self):
        user = self.create_user()
        response = self.create_user(username=user['username'])
        self.assertEqual(400, response.get('status_code'))
        self.assertEqual('User exist with: %s' % user['username'],
                         response.get('message'))

    def test_create_ssh(self):
        user = self.create_user()
        ssh = self.create_ssh(user['id'])

    def test_init(self):
        sys.argv = ['my_dev/runner.py',
                    'my', '--init', '-u', 'user', '-p', 'password',
                    '-e', 'email']
        runner.main()
