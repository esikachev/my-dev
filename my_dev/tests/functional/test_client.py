import testtools

import my_dev.users as users


class TestClient(testtools.TestCase):

    def setUp(self):
        super(TestClient, self).setUp()
        self.user = users.Users()

    def test_client(self):
        user = self.user.create('test-user', 'user@user.com', 'password')
        id = self.user.get(user['id'])
        name = self.user.get(user['username'])
        self.assertEqual(id, name)
        self.user.delete(user['id'])
