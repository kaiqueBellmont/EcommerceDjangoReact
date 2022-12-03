# external imports
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

# internal imports
from .models import (
    Product, Review, Order, OrderItem, ShippingAddress
)

"""
Notes:
    serializers are needed to transform python objects into JSON, and do the reverse process too.
"""


class UserSerializer(serializers.ModelSerializer):
    """
    Simple user serielizer class
    """
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name


class UserSerializerWithToken(UserSerializer):
    """
    User with JWT token serielizer
    """
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class ProductSerializer(serializers.ModelSerializer):
    """
    Simple Product Serielizer class
    """
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'user',
            'name',
            'image',
            'brand',
            'category',
            'description',
            'rating',
            'numReviews',
            'price',
            'countInStock',
            '_id',
            'reviews'
        )

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data


class ReviewSerializer(serializers.ModelSerializer):
    """
    Simple Review Serielizer class
    """

    class Meta:
        model = Review
        fields = (
            'product',
            'user',
            'name',
            'rating',
            'comment',
            '_id'
        )

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data


class OrderSerializer(serializers.ModelSerializer):
    """
    Simple Review Serielizer class
    """
    orderItems = serializers.SerializerMethodField(read_only=True)
    shippingAddress = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = (
            'user',
            'paymentMethod',
            'taxPrice',
            'shippingPrice',
            'totalPrice',
            'isPaid',
            'paidAt',
            'isDelivered',
            'deliveredAt',
            '_id',
        )

    def get_orderItems(self, obj):
        items = obj.orderitem_set.all()
        serializer = OrderItemSerializer(items, many=True)
        return serializer.data

    def get_shippingAddress(self, obj):
        try:
            address = ShippingAddressSerializer(
                obj.shippingaddress, many=False).data
        except:
            address = False
        return address

    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Simple OrderItem serielizer class
    """

    class Meta:
        model = OrderItem
        fields = (
            'product',
            'order',
            'name',
            'qty',
            'price',
            'image',
        )


class ShippingAddressSerializer(serializers.ModelSerializer):
    """
    simple ShippingAddress serielizer class
    """

    class Meta:
        model = ShippingAddress
        fields = (
            'order',
            'address',
            'city',
            'postalCode',
            'country',
            'shippingPrice',
        )
