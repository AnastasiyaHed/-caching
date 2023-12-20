from django.urls import path
from .views import book_list
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# Определение схемы Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Your API",
      default_version='v1',
      description="Your API description",
      terms_of_service="https://www.yourapp.com/terms/",
      contact=openapi.Contact(email="contact@yourapp.com"),
      license=openapi.License(name="Your License"),
   ),
   public=True,
)



urlpatterns = [
    path('', book_list, name='book_list'),
    #path('books/', book_list, name='book_list'),
    # маршруты для Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

