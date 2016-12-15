import json
import requests


class Users(object):

    def create(self, **kwargs):
        """Create new user"""
        url = 'http://localhost:5000/users'
        for (key, value) in kwargs.items():
            data += (key, value)
        create_user = requests.post(url, data=json.dump(data))
        return create_user.json()

    def get(self, user_id):
        """Get user information"""
        url = 'http://localhost:5000/users/%s' % user_id
        get_user = requests.get(url)
        return get_user.json()
