from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from rest_framework import mixins

from ..models import PostAttachments
from ..serializers import PostAttachmentsSerializer

# Create your views here.

class PostAttachmentsListView(generics.ListCreateAPIView):
    queryset = PostAttachments.objects.all()
    serializer_class = PostAttachmentsSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields  = '__all__'
    ordering_fields = '__all__'

class PostAttachmentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostAttachments
    serializer_class = PostAttachmentsSerializer