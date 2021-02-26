from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from comment.views.pagination import CustomPageNumberPagination

from comment.models import CommentLike
from comment.serializers import CommentLikeSerializer

# Create your views here.

class CommentLikeListView(generics.ListCreateAPIView):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    pagination_class = CustomPageNumberPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields  = '__all__'
    ordering_fields = '__all__'

class CommentLikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentLike
    serializer_class = CommentLikeSerializer

