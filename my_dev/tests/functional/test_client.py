import sys

import testtools

import my_dev.users as users
from my_dev import runner


class TestClient(testtools.TestCase):

    def setUp(self):
        super(TestClient, self).setUp()
        self.user = users.Users()

    def test_client(self):
        user = self.user.create('test-user', 'user@user.com', 'password')
        user_by_id = self.user.get(user['id'])
        user_by_name = self.user.get(user['username'])
        self.assertEqual(user_by_id, user_by_name)
        self.user.delete(user['id'])

    def test_init(self):
        sys.argv = ['my_dev/runner.py',
                    'my', 'init', '-u', 'user', '-p', 'password',
                    '-e', 'email']
        runner.main()
