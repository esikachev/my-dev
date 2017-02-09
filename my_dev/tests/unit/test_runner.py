import sys

import testtools
import mock

from my_dev import runner
from my_dev.tests import utils


class TestRunner(testtools.TestCase):
    def setUp(self):
        super(TestRunner, self).setUp()
        self.username = utils.rand_name('user')
        self.email = utils.rand_name('email')

    @mock.patch('my_dev.users.Users')
    @mock.patch('my_dev.base.Base')
    def test_runner(self, mock_base, mock_users):
        sys.argv = ['my_dev/runner.py',
                    'my', '--init', '-u', self.username, '-p', 'password',
                    '-e', self.email]
        runner.main()
