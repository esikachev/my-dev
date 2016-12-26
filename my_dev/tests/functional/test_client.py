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
        self.user.get(user['id'])
        self.user.delete(user['id'])

    def test_init(self):
        sys.argv = ['my_dev/runner.py',
                    'my', 'init', '-u', 'us', '-p', 'pass', '-e', 'email']
        runner.main()

        # we need this line for travis-ci
        print "Test: init - passed"
