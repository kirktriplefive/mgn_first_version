from rest_framework import viewsets

from .serializers import (
    PostSerializer, 
    CommentSerializer, 
    CommentListRetrieveSerializer,
    PostDetailSerializer
)
from ..models import Post, Comments


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    action_to_serializer = {
        "retrieve": PostDetailSerializer
    }
    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    action_to_serializer = {
        "list": CommentListRetrieveSerializer,
        "retrieve": CommentListRetrieveSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )
