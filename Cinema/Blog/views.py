from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from .models import blog, post, Comment
from .serializers import BlogSerializer, PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class BlogViewSet(viewsets.ModelViewSet):
    queryset = blog.objects.all().order_by('-date_created')
    serializer_class = BlogSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        blog_id = request.query_params.get("blog")
        if blog_id:
            posts = self.queryset.filter(blog_id=blog_id)
        else:
            posts = self.queryset.all()
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
    
class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]  # همه می‌توانند ببینند

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id).order_by('-date_created')