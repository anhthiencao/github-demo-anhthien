from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from rest_framework import mixins

from ..models import PostInteract
from ..serializers import PostInteractSerializer

# Create your views here.

class PostInteractListView(generics.ListCreateAPIView):
    queryset = PostInteract.objects.all()
    serializer_class = PostInteractSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields  = '__all__'
    ordering_fields = '__all__'

class PostInteractDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostInteract
    serializer_class = PostInteractSerializer