from base.models import *
import T
import requests
import jsonpath


class BaseMixin:
    def make_user(
            self,
            name='user123',
            email='user@gmail.com',
            password='user"$123'
    ):
        return User.objects.create_user(
            name=name,
            email=email,
            password=password
        )


class BaseTestSetup(TestCase):
    def setUp(self):
        return super().setUp()


"""
def test_get_products():
    products = requests.request(method='GET', url='http://127.0.0.1:8000/api/products/')
    print(products)
    assert products
"""
