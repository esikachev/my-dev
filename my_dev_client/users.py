from flask import Flask
import requests

app = Flask(__name__)


class Users(object):

    @app.route('/users', methods=['POST'])
    def create(self, data=None):
        """Create new user"""
        url = 'http://localhost:5000/users'
        create_user_request = requests.post(url, data=data)
        request_status = (create_user_request.status_code == requests.codes.ok)
        if request_status is False:
            raise Exception("Bad request in creating the user")
        else:
            return create_user_request

    @app.route('/get_user', methods=['GET'])
    def get(self, user_id):
        """Get user information"""
        url = 'http://localhost:5000/users/ %s' % user_id
        get_user_request = requests.get(url)
        request_status = (get_user_request.status_code == requests.codes.ok)
        if request_status is False:
            raise Exception("Bad request in getting the user")
        else:
            return get_user_request
g