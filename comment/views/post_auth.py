from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics,filters
from comment.views.pagination import CustomPageNumberPagination

from comment.models import PostAuth
from comment.serializers import PostAuthSerializer

# Create your views here.

class PostAuthListView(generics.ListCreateAPIView):
    queryset = PostAuth.objects.all()
    serializer_class = PostAuthSerializer
    pagination_class = CustomPageNumberPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields  = '__all__'
    ordering_fields = '__all__'

class PostAuthDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostAuth
    serializer_class = PostAuthSerializer



