from rest_framework import serializers
from . import models

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('author', 'text', 'created_at', 'approved_comment')