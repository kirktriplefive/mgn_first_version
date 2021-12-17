from rest_framework import serializers
from ..models import Post, Comments

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class PostDetailSerializer(serializers.ModelSerializer):

    posts = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields ='__all__'
    
    @staticmethod 
    def get_posts(obj):
        return CommentSerializer(Comments.objects.filter(post=obj), many=True).data


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields ='__all__'


class CommentListRetrieveSerializer(serializers.ModelSerializer):

    post = PostSerializer()

    class Meta:
        model = Comments
        fields ='__all__'

    
