from django.urls import path
from .api_views import ProductListAPIView, ProductCreateAPIView,ProductDetailAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('product/create/', ProductCreateAPIView.as_view(), name='create'),
    path('product/<str:id>/', ProductDetailAPIView.as_view(), name='detail')
]
