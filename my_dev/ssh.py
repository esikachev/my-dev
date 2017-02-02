import client


class Ssh(object):

    def __init__(self, user_id):
        self.client = client.Client()
        self.user_id = user_id
        self.prefix = '/users/%s/ssh' % self.user_id

    def create(self, host=None, ssh_username=None, ssh_password=None,
               alias=None):
        data = {
            "user_id": self.user_id,
            "host": host,
            "ssh_username": ssh_username,
            "ssh_password": ssh_password,
            "alias": alias
        }
        request_create = self.client.post(self.prefix, data=data)
        return request_create

    def get(self, ssh_id):
        request_get = self.client.get(self.prefix, ssh_id)
        return request_get

    def delete(self, ssh_id):
        request_delete = self.client.delete(self.prefix, ssh_id)
        return request_delete
