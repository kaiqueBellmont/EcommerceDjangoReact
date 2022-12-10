from drf_yasg import openapi


order__id = openapi.Schema(type=openapi.TYPE_INTEGER)
createdAt = openapi.Schema(type=openapi.FORMAT_DATETIME, example="2022-12-10T18:17:35.623624Z")
updatedAt = openapi.Schema(type=openapi.FORMAT_DATETIME, example="2022-12-10T18:17:35.623624Z")
