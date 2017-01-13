import client


class Ssh(object):

    def __init__(self):
        self.client = client.Client()
        self.prefix = '/users'

    def create(self, user_id, username, password, alias, host):
        data = {
            "user_id": user_id,
            "username": username,
            "password": password,
            "alias": alias,
            "host": host
        }
        prefix = self._get_prefix(user_id)
        request_create = self.client.post(prefix, data=data)
        return request_create

    def get(self, ssh_id, user_id):
        prefix = self._get_prefix(user_id)
        request_get = self.client.get(prefix, ssh_id)
        return request_get

    def delete(self, ssh_id, user_id):
        prefix = self._get_prefix(user_id)
        request_delete = self.client.delete(prefix, ssh_id)
        return request_delete

    def _get_prefix(self, user_id):
        return '%s/%s/ssh' % (self.prefix, user_id)
