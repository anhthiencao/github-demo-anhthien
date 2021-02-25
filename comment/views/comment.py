from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from rest_framework import mixins

from ..models import Comment
from ..serializers import CommentSerializer

# Create your views here.

class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields  = '__all__'
    ordering_fields = '__all__'

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment
    serializer_class = CommentSerializer