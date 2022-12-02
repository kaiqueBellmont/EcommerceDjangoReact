from django.contrib import admin

from .models import (
    Product, Review, Order, OrderItem, ShippingAddress
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        '_id',
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
        'createdAt',
        'updatedAt',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        '_id',
        'product',
        'user',
        'name',
        'rating',
        'comment',
        'createdAt',
        'updatedAt',
   )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        '_id',
        'user',
        'paymentMethod',
        'taxPrice',
        'shippingPrice',
        'totalPrice',
        'isPaid',
        'paidAt',
        'isDelivered',
        'deliveredAt',
        'createdAt',
        'updatedAt'
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        '_id',
        'product',
        'order',
        'name',
        'qty',
        'price',
        'image',
        'createdAt',
        'updatedAt',
    )


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = (
        '_id',
        'order',
        'address',
        'city',
        'postalCode',
        'country',
        'shippingPrice',
        'createdAt',
        'updatedAt',
    )
