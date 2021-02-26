from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from comment.views.pagination import CustomPageNumberPagination

from comment.models import Comment
from comment.serializers import CommentSerializer

# Create your views here.

class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CustomPageNumberPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields  = '__all__'
    ordering_fields = '__all__'

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment
    serializer_class = CommentSerializer



