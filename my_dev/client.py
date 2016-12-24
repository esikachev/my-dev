from requests import codes
from requests import delete
from requests import get
from requests import exceptions as exc
from requests import post

URL = 'http://localhost:5000'


class Client(object):

    def _post(self, *args, **kwargs):
        return post(*args, **kwargs)

    def _get(self, *args):
        return get(*args)

    def _delete(self, *args):
        return delete(*args)

    def post(self, prefix, data):
        create_request = self._post(self._get_url(prefix), json=data)
        request_status = (create_request.status_code == codes.ok)
        if request_status:
            return create_request.json()
        else:
            raise exc.RequestException("Bad POST request")

    def get(self, prefix, id):
        get_request = self._get(self._get_url(prefix, data=id))
        request_status = (get_request.status_code == codes.ok)
        if request_status:
            return get_request.json()
        else:
            raise exc.RequestException("Bad GET request")

    def delete(self, prefix, id):
        delete_request = self._delete(self._get_url(prefix, data=id))
        request_status = (delete_request.status_code == codes.ok)
        if request_status:
            return delete_request.json()
        else:
            raise exc.RequestException("Bad DELETE request")

    def _get_url(self, prefix, data=''):
        return '%s%s/%s' % (URL, prefix, data)
