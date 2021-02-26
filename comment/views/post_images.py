from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics,filters
from comment.views.pagination import CustomPageNumberPagination

from comment.models import PostImages
from comment.serializers import PostImagesSerializer
# Create your views here.

class PostImagesListView(generics.ListCreateAPIView):
    queryset = PostImages.objects.all()
    serializer_class = PostImagesSerializer
    pagination_class = CustomPageNumberPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields  = '__all__'
    ordering_fields = '__all__'

class PostImagesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostImages
    serializer_class = PostImagesSerializer



