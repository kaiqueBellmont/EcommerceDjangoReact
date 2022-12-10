from drf_yasg import openapi
from .order_base import order__id, createdAt, updatedAt
from swagger.users.users_base import user

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
