from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from rest_framework import mixins

from ..models import PostImages
from ..serializers import PostImagesSerializer

# Create your views here.

class PostImagesListView(generics.ListCreateAPIView):
    queryset = PostImages.objects.all()
    serializer_class = PostImagesSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields  = '__all__'
    ordering_fields = '__all__'

class PostImagesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostImages
    serializer_class = PostImagesSerializer