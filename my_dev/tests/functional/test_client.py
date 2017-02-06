import sys

import testtools

from my_dev.tests import utils
import my_dev.users as users


class TestClient(testtools.TestCase):

    def setUp(self):
        super(TestClient, self).setUp()
        self.user = users.Users()

    def test_client(self):
        user_name = utils.rand_name('test')
        user_email = utils.rand_name('test')
        user_pass = utils.rand_name('test')
        user = self.user.create(user_name, user_email, user_pass)
        user_by_id = self.user.get(user['id'])
        user_by_name = self.user.get(user['username'])
        self.assertEqual(user_by_id, user_by_name)
        self.user.delete(user['id'])

    def test_create_already_existed_user(self):
        user_name = utils.rand_name('test')
        user_email = utils.rand_name('test')
        user_pass = utils.rand_name('test')
        self.user.create(user_name, user_email, user_pass)
        new_user_email = utils.rand_name('test')
        new_user_pass = utils.rand_name('test')
        response = self.user.create(user_name, new_user_email, new_user_pass)
        self.assertEqual(400, response.get('status_code'))
        self.assertEqual('User exist with: %s' % user_name,
                         response.get('message'))
