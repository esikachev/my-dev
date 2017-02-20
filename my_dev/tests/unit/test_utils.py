import mock
import testtools

from my_dev import utils


class TestUtils(testtools.TestCase):
    def test_utils(self):
        open_name = '%s.open' % __name__
        with mock.patch(open_name, create=True) as mock_open:
            mock_open.return_value = mock.MagicMock(spec=file)
            utils.write_to_config('test_user', 'test_host')
