from django.shortcuts import render
from rest_framework import viewsets
from comment.models import Comment
from comment.serializers import CommentSerializer

# Create your views here.

class CommentViews(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer