import sys
from requests import exceptions as exc
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
        user_email = utils.rand_name('test@')
        user_password = utils.rand_name('pass')
        user = self.user.create(user_name, user_email, user_password)
        self.user.get(user['id'])
        self.user.delete(user['id'])

    def test_init(self):
        sys.argv = ['my_dev/runner.py',
                    'my', '--init', '-u', 'user', '-p', 'password',
                    '-e', 'email']
        runner.main()

    def test_create_already_existed_user(self):
        msg_exist = None
        user_name = utils.rand_name('test')
        user_email = utils.rand_name('user@')
        user_password = utils.rand_name('pass')
        error_message = "User exist with username: %s" % user_name
        self.user.create(user_name, user_email, user_password)
        try:
            new_user_email = utils.rand_name('new_user@')
            new_user_password = utils.rand_name('new_pass')
            self.user.create(user_name, new_user_email, new_user_password)
        except exc.RequestException as e:
            output_msg = str(e)
            for msg in output_msg:
                if msg.lower() == error_message.lower():
                    self.assertEqual(error_message.lower(), msg.lower())
                    msg_exist = True
            if not msg_exist:
                raise BaseException('User exist with username: %s' % user_name)
