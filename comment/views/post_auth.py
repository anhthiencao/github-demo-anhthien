from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from rest_framework import mixins

from ..models import PostAuth
from ..serializers import PostAuthSerializer

# Create your views here.

class PostAuthListView(generics.ListCreateAPIView):
    queryset = PostAuth.objects.all()
    serializer_class = PostAuthSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields  = '__all__'
    ordering_fields = '__all__'

class PostAuthDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostAuth
    serializer_class = PostAuthSerializer