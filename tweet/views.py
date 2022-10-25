from rest_framework import viewsets

from .models import Tweet
from .serializers import TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    """
    ViewSet designed for Tweet model

    Only 'Get' and 'Post' method is allowed cause we need 'list' and 'create' APIs
    """
    allowed_methods = ['get', 'post']
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
