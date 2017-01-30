from oslo_config import cfg
from requests import delete
from requests import get
from requests import post

CONF = cfg.CONF


class Client(object):

    def _post(self, *args, **kwargs):
        return post(*args, **kwargs)

    def _get(self, *args):
        return get(*args)

    def _delete(self, *args):
        return delete(*args)

    def post(self, prefix, data):
        create_request = self._post(self._get_url(prefix), json=data)
        return create_request.json()

    def get(self, prefix, id):
        get_request = self._get(self._get_url(prefix, data=id))
        return get_request.json()

    def delete(self, prefix, id):
        delete_request = self._delete(self._get_url(prefix, data=id))
        return delete_request.json()

    def _get_url(self, prefix, data=''):
        return '%s%s/%s' % (CONF.host, prefix, data)
