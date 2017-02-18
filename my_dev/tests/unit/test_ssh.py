import mock
import testtools


from my_dev import ssh


class TestSsh(testtools.TestCase):
    @mock.patch('my_dev.client.Client', return_value='client')
    def test_init(self, mock_client):
        ssh_client = ssh.Ssh('user_id')
        self.assertEqual('client', ssh_client.client)
        self.assertEqual('user_id', ssh_client.user_id)
        self.assertEqual('/users/user_id/ssh', ssh_client.prefix)
