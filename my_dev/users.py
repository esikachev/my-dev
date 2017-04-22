import client


class Users(Client):

    def __init__(self):
        self.prefix = '/users'

    def create(self, username, password, email):
        data = {
            "username": username,
            "password": password,
            "email": email
        }
        request_create = self.post(self.prefix, data=data)
        return request_create

    def get(self, user_id):
        request_get = self.get(self.prefix, user_id)
        return request_get

    def delete(self, user_id):
        request_delete = self.delete(self.prefix, user_id)
        return request_delete

    def get_id(self, name):
        request_get = self.client.get(self.prefix, name)
        return request_get['id']
