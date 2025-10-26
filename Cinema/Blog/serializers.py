from rest_framework import serializers
from .models import blog, post, Comment

# This is the serializer class that will be used to serialize the blog, post, and comment models
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'content', 'username', 'date_created']

    def get_username(self, obj):
        return obj.user.username if obj.user else "کاربر ناشناس"
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = post
        fields = ['id', 'blog', 'title', 'content', 'image', 'date_created', 'comments']

class BlogSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = blog
        fields = ['id', 'name', 'description', 'image', 'date_created', 'posts']
