from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from comment.views.pagination import CustomPageNumberPagination

from comment.models import PostInteract
from comment.serializers import PostInteractSerializer

# Create your views here.

class PostInteractListView(generics.ListCreateAPIView):
    """
    Get all comments, create a new comment, get comments by... 
    """
    queryset = PostInteract.objects.all()
    serializer_class = PostInteractSerializer
    pagination_class = CustomPageNumberPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields  = '__all__'
    ordering_fields = '__all__'

class PostInteractDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostInteract
    serializer_class = PostInteractSerializer




