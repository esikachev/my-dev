import client
from requests import exceptions as exc

from my_dev import config


class Users(object):

    def __init__(self):
        self.client = client.Client()
        self.prefix = '/users'

    def create(self, username, password, email):
        data = {
            "username": username,
            "password": password,
            "email": email
        }
        request_create = self.client.post(self.prefix, data=data)
        if (request_create.text == config.USER_EXISTS.format(
                'username', data['username'])
            or request_create.text == config.USER_EXISTS.format(
                'email', data['email'])):
            raise exc.RequestException(request_create.text)
        return request_create

    def get(self, user_id):
        request_get = self.client.get(self.prefix, user_id)
        if request_get.text == config.USER_DOESNT_EXIST.format(id):
            raise exc.RequestException(request_get.text)
        return request_get

    def delete(self, user_id):
        request_delete = self.client.delete(self.prefix, user_id)
        if request_delete.text == config.USER_DOESNT_EXIST.format(id):
            raise exc.RequestException(request_delete.text)
        return request_delete

    def get_id(self, name):
        request_get = self.client.get(self.prefix, name)
        return request_get['id']
