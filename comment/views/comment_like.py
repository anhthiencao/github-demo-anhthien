from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from rest_framework import mixins

from ..models import CommentLike
from ..serializers import CommentLikeSerializer

# Create your views here.

class CommentLikeListView(generics.ListCreateAPIView):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields  = '__all__'
    ordering_fields = '__all__'

class CommentLikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentLike
    serializer_class = CommentLikeSerializer