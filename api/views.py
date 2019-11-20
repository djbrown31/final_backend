from rest_framework import generics

import models
from . import serializers

class CommentListView(generics.ListAPIView):
    queryset = models.Comment
    serializer_class = serializers.CommentSerializer
