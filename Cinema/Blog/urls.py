from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet)  # برای لیست و جزئیات بلاگ
router.register(r'posts', views.PostViewSet)  # برای پست‌ها (مربوط به بلاگ)

urlpatterns = [
    path('api/', include(router.urls)),

    # اضافه کردن کامنت برای یک پست خاص
    path('api/posts/<int:post_id>/comment/', views.CommentCreateView.as_view(), name='post-comment'),

    # گرفتن تمام کامنت‌های یک پست (برای نمایش در جزئیات بلاگ)
    path('api/posts/<int:post_id>/comments/', views.CommentListView.as_view(), name='post-comments'),
]
