from rest_framework.decorators import api_view
from rest_framework.response import Response

# local imports
from .models import Product
from .serielizers import ProductSerializer

@api_view(['GET'])
def get_routes(request):
    routes = [
        "api/tananan"
    ]
    return Response(routes)


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def get_product(request, pk):
    product = Product.objects.get(_id=pk)
    serielizer = ProductSerializer(product, many=False)
    return Response(serielizer.data)
