import client


class Users(Client):

    def __init__(self):
        self.prefix = '/users'

    def create(self, username, email, password):
        data = {
            "username": username,
            "email": email,
            "password": password
        }
        request_create = self.post(self.prefix, data=data)
        return request_create

    def get(self, user_id):
        request_get = self.get(self.prefix, user_id)
        return request_get

    def delete(self, user_id):
        request_delete = self.delete(self.prefix, user_id)
        return request_delete
