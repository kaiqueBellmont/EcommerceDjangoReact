import os
import pytest

from .base_test import BaseTestSetup, User
import requests
import jsonpath


class UserEndpointsTest(BaseTestSetup):
    base_url = 'http://127.0.0.1:8000/api/users/'
    base_headers = os.environ.get('TOKEN')
    base_data = ''

    @pytest.mark.django_db
    def test_get_users(self):
        res = res = requests.get(
            url='http://127.0.0.1:8000/api/users/',
            headers={
                'Authorization': os.environ.get('TOKEN'),
            }
        )
        users = res.json()
        import pdb
        pdb.set_trace()

    @pytest.mark.django_db(transaction=False, reset_sequences=True)
    def test_user_register(self):
        new_user = {
            "name": "UserTest",
            "email": "userTest@gmail.com",
            "password": "UserTest@$123"
        }
        res = requests.post(
            url='http://127.0.0.1:8000/api/users/register/',
            data=new_user
        )
        assert res.status_code == 200 or 400

