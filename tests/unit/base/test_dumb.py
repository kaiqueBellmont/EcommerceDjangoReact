import requests


def test_dumb():
    assert True


def test_get_products():
    products = requests.request(method='GET', url='http://127.0.0.1:8000/api/products/')
    print(products)
    assert products
