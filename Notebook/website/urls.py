from django.urls import path 
from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('note/', views.create_note, name='notebook'),
    path('notes/', views.note_list, name='note_list'),
    path('<int:pk>/', views.note_detail, name='note_detail'),
    path('<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('<int:pk>/delete/', views.note_delete, name='note_delete'),
]
