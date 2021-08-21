from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from .serializer import ProductSerializer
from ..models import Product
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [SearchFilter]
    search_fields = ['title', 'parameters']


class ProductCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
