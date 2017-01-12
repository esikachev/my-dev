from requests import exceptions as exc
import testtools

from my_dev.tests.functional import utils
import my_dev.users as users


class TestClient(testtools.TestCase):

    def setUp(self):
        super(TestClient, self).setUp()
        self.user = users.Users()

    def test_client(self):
        user_name = utils.rand_name('test')
        user = self.user.create(user_name, 'user@user.com', 'password')
        self.user.get(user['id'])
        self.user.delete(user['id'])

    def test_create_already_existed_user(self):
        msg_exist = None
        user_name = utils.rand_name('test')
        error_message = "User exist with username: %s" % user_name
        self.user.create(user_name, 'user@user.com', 'password')
        try:
            self.user.create(user_name, 'new@user.com', 'qwerty')
        except exc.RequestException as e:
            output_msg = str(e).splitlines()
            for msg in output_msg:
                if msg.lower() == error_message.lower():
                    self.assertEqual(error_message.lower(), msg.lower())
                    msg_exist = True
            if not msg_exist:
                raise BaseException('User with already existing username %s '
                                    'have been created' % user_name)
