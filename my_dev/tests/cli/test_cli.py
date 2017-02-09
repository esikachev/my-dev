import sys

import mock
import testtools

from my_dev import runner
from my_dev.tests import utils


class TestCli(testtools.TestCase):
    def setUp(self):
        super(TestCli, self).setUp()
        username = utils.rand_name('user')
        email = utils.rand_name('email')
        self.cmd = 'sshpass -p test_pass ssh user@127.0.0.1'
        self.init_user(username, email)

    def init_user(self, username, email):
        sys.argv = ['my_dev/runner.py',
                    'my', '--init', '-u', username, '-p', 'password',
                    '-e', email]
        runner.main()

    @mock.patch('os.system')
    @mock.patch('__builtin__.raw_input', return_value='alias')
    @mock.patch('my_dev.base.Base.enter_pass', return_value='test_pass')
    def test_workflow(self, mock_pass, mock_alias, mock_os):
        sys.argv = ['my', 'ssh', 'user@127.0.0.1']
        runner.main()
        mock_os.assert_called_with(self.cmd)

    @mock.patch('os.system')
    @mock.patch('__builtin__.raw_input', return_value='alias')
    @mock.patch('my_dev.base.Base.enter_pass', return_value='test_pass')
    def test_workflow_host(self, mock_pass, mock_alias, mock_os):
        sys.argv = ['my', 'ssh', 'user@127.0.0.1']
        runner.main()
        mock_os.assert_called_with(self.cmd)
        sys.argv = ['my', 'ssh', '127.0.0.1']
        runner.main()
        mock_os.assert_called_with(self.cmd)

    @mock.patch('os.system')
    @mock.patch('__builtin__.raw_input', return_value='alias')
    @mock.patch('my_dev.base.Base.enter_pass', return_value='test_pass')
    def test_workflow_alias(self, mock_pass, mock_alias, mock_os):
        sys.argv = ['my', 'ssh', 'user@127.0.0.1']
        runner.main()
        mock_os.assert_called_with(self.cmd)
        sys.argv = ['my', 'ssh', 'alias']
        runner.main()
        mock_os.assert_called_with(self.cmd)
