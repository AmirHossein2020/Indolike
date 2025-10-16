from django.urls import path
from . import views

# This file defines the URL patterns for the accounts app.
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
]
