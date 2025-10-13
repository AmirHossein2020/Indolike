from django.urls import path 
from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('note/', views.create_note, name='notebook'),
    path('notes/', views.note_list, name='note_list'),
]
