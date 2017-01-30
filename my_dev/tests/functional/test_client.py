from requests import exceptions as exc
import sys

import testtools

from my_dev.tests.functional import utils
import my_dev.users as users
from my_dev import runner


class TestClient(testtools.TestCase):

    def setUp(self):
        super(TestClient, self).setUp()
        self.user = users.Users()

    def test_client(self):
        user_name = utils.rand_name('test')
        user_email = utils.rand_name('test')
        user_pass = utils.rand_name('test')
        user = self.user.create(user_name, user_email, user_pass)
        self.user.get(user['id'])
        user = self.user.create('test-user', 'user@user.com', 'password')
        user_by_id = self.user.get(user['id'])
        user_by_name = self.user.get(user['username'])
        self.assertEqual(user_by_id, user_by_name)
        self.user.delete(user['id'])

    def test_create_already_existed_user(self):
        msg_exist = None
        user_name = utils.rand_name('test')
        user_email = utils.rand_name('test')
        user_pass = utils.rand_name('test')
        error_message = "User exist with username: %s" % user_name
        self.user.create(user_name, user_email, user_pass)
        new_user_email = utils.rand_name('test')
        new_user_pass = utils.rand_name('test')
        response = self.user.create(user_name, new_user_email, new_user_pass)
        print response.status_code,

    def test_init(self):
        sys.argv = ['my_dev/runner.py',
                    'my', '--init', '-u', 'user', '-p', 'password',
                    '-e', 'email']
        runner.main()
