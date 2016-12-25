import client


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
        return request_create

    def get(self, user_id):
        request_get = self.client.get(self.prefix, user_id)
        return request_get

    def delete(self, user_id):
        request_delete = self.client.delete(self.prefix, user_id)
        return request_delete
