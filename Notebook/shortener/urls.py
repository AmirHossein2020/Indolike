from django.urls import path
from . import views

# URL patterns for the URL shortener app
urlpatterns = [
    path('api/', views.shorten_url_api, name='shorten_url_api'),
    path('<str:short_code>/', views.redirect_short_url, name='redirect_short_url'),
]
