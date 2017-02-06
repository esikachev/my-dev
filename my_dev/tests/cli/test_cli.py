from io import StringIO
import sys

import mock
import testtools

from my_dev import runner
from my_dev.tests import utils


class TestCli(testtools.TestCase):
    def setUp(self):
        super(TestCli, self).setUp()
        self.username = utils.rand_name('user')
        self.email = utils.rand_name('email')

    def init_user(self):
        sys.argv = ['my_dev/runner.py',
                    'my', '--init', '-u', self.username, '-p', 'password',
                    '-e', self.email]
        runner.main()

    def test_init(self):
        self.init_user()

    @mock.patch('getpass.getpass')
    def test_create_ssh(self, mock_getpass):
        self.init_user()
        sys.argv = ['my', 'ssh', 'qa@172.18.79.150']
        mock_getpass.return_value = 'swordfish'
        runner.main()
