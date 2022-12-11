import django.core.serializers.json
from drf_yasg import openapi

from base.serializers import OrderSerializer
from swagger.users.users_base import user
from .order_base import order__id, createdAt, updatedAt

orderItems = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "product": openapi.Schema(type=openapi.TYPE_INTEGER, description="product_id", example="1"),
        "name": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="product_name",
            example="Sony Playstation 4 Pro White Version"
        ),
        "image": openapi.Schema(
            type=openapi.TYPE_STRING,
            description="product_image",
            example="https://eukiak-bucket-demo.s3.amazonaws.com/playstation.jpg"
        ),
        "price": openapi.Schema(type=openapi.TYPE_STRING, description="product_price", example="500.00"),
        "countInStock": openapi.Schema(type=openapi.TYPE_INTEGER, description="countInStock", example="8"),
        "qty": openapi.Schema(type=openapi.TYPE_INTEGER, description="qty", example="1"),
    },
    required=[]

)

shippingAddress = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "address": openapi.Schema(type=openapi.TYPE_STRING, example="adress 123"),
        "city": openapi.Schema(type=openapi.TYPE_STRING, example="city anywhere"),
        "postalCode": openapi.Schema(type=openapi.TYPE_STRING, example="123456789"),
        "country": openapi.Schema(type=openapi.TYPE_STRING, example="brazil"),
    },
    required=[]

)

paymentMethod = openapi.Schema(
    type=openapi.TYPE_STRING,
    example="paypal"
)

itemsPrice = openapi.Schema(
    type=openapi.TYPE_STRING,
    example="500.00"
)
shippingPrice = openapi.Schema(
    type=openapi.TYPE_STRING,
    example="10.00"
)
taxPrice = openapi.Schema(
    type=openapi.TYPE_STRING,
    example="10.00"
)
totalPrice = openapi.Schema(
    type=openapi.TYPE_STRING,
    example="520.00"
)

isPaid = openapi.Schema(
    type=openapi.TYPE_BOOLEAN,
    example=False
)

paidAt = openapi.Schema(
    type=openapi.FORMAT_DATETIME,
    example="2022-12-12T15:15:45.745275Z")

is_delivered = openapi.Schema(
    type=openapi.TYPE_BOOLEAN,
    example=False
)

deliveredAt = openapi.Schema(
    type=openapi.FORMAT_DATETIME,
    example="2022-12-15T15:00:00.000000Z")

order_items_response = {
    "_id": order__id,
    'orderItems': openapi.Schema(type=openapi.TYPE_ARRAY, items=orderItems),
    "shippingAddress": shippingAddress,
    "user": user,
    "createdAt": createdAt,
    "updatedAt": updatedAt,
    "paymentMethod": paymentMethod,
    "taxPrice": taxPrice,
    "shippingPrice": shippingPrice,
    "totalPrice": totalPrice,
    "isPaid": isPaid,
    "paidAt": paidAt,
    "isDelivered": is_delivered,
    "deliveredAt": deliveredAt
}

data = {'orderItems':
    [
        {
            'product': 1,
            'name': 'Sony Playstation 4 Pro White Version',
            'image': 'https://eukiak-bucket-demo.s3.amazonaws.com/playstation.jpg',
            'price': '500.00',
            'countInStock': 5, 'qty': 1
        }
    ],
    'shippingAddress':
        {
            'address': 'rua ',
            'city': 'BH',
            'postalCode': '31998320',
            'country': 'brazil'
        },
    'paymentMethod': 'PayPal',
    'itemsPrice': '500.00',
    'shippingPrice': '0.00',
    'taxPrice': '41.00',
    'totalPrice': '541.00'
}

response_schema_dict = {
    "200": openapi.Response(
        description="Complete Response example:",
        examples={
            "application/json":
                {
                    "_id": 27,
                    "orderItems": [
                        {
                            "_id": 23,
                            "createdAt": "2022-12-10T19:49:16.296011Z",
                            "updatedAt": "2022-12-10T19:49:16.296025Z",
                            "name": "Sony Playstation 4 Pro White Version",
                            "qty": 1,
                            "price": "500.00",
                            "image": "https://eukiak-bucket-demo.s3.amazonaws.com/playstation.jpg",
                            "product": 1,
                            "order": 27
                        }
                    ],
                    "shippingAddress": False,
                    "user": {
                        "id": 1,
                        "_id": 1,
                        "username": "kaiquebellmont@gmail.com",
                        "email": "kaiquebellmont@gmail.com",
                        "name": "kaique",
                        "isAdmin": False
                    },
                    "createdAt": "2022-12-10T19:49:15.638635Z",
                    "updatedAt": "2022-12-10T19:49:15.638677Z",
                    "paymentMethod": "paypal",
                    "taxPrice": "10.00",
                    "shippingPrice": "54.00",
                    "totalPrice": "564.00",
                    "isPaid": False,
                    "paidAt": None,
                    "isDelivered": False,
                    "deliveredAt": False
                }
        }
    )
}

response = response_schema_dict
