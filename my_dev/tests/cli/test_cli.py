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

    @mock.patch('my_dev.base.Base.enter_pass', return_value='test_pass')
    def test_workflow(self, mock_pass):
        self.init_user()
        sys.argv = ['my', 'ssh', 'user@127.0.0.1']
        runner.main()
        sys.argv = ['my', 'ssh', '127.0.0.1']
        runner.main()
        sys.argv = ['my', 'ssh', 'user@127.0.0.1']
        runner.main()
