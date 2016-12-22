import testtools

import my_dev_client.users as users


class TestClient(testtools.TestCase):

    def setUp(self):
        super(TestClient, self).setUp()
        self.user = users.Users()

    def test_client(self):
        user = self.user.create('test-user', 'user@user.com')
        self.user.get(user['id'])
        self.user.delete(user['id'])
