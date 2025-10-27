from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet)  
router.register(r'posts', views.PostViewSet)  

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/posts/<int:post_id>/comments/', views.CommentListCreateView.as_view(), name='post-comments'),
    
]
