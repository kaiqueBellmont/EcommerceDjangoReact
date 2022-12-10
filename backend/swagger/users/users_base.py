from drf_yasg import openapi

user = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        "_id": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        "username": openapi.Schema(type=openapi.TYPE_STRING, example="kaique bellmont"),
        "email": openapi.Schema(type=openapi.FORMAT_EMAIL, example="kaiquebellmont@gmail.com"),
        "name": openapi.Schema(type=openapi.TYPE_STRING, example="kaique cairan"),
        "isAdmin": openapi.Schema(type=openapi.TYPE_BOOLEAN, example=False)
    }
)
