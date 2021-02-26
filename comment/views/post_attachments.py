from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics,filters
from comment.views.pagination import CustomPageNumberPagination

from comment.models import PostAttachments
from comment.serializers import PostAttachmentsSerializer
# Create your views here.

class PostAttachmentsListView(generics.ListCreateAPIView):
    queryset = PostAttachments.objects.all()
    serializer_class = PostAttachmentsSerializer
    pagination_class = CustomPageNumberPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields  = '__all__'
    ordering_fields = '__all__'

class PostAttachmentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostAttachments
    serializer_class = PostAttachmentsSerializer





