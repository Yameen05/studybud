from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),  # API root view
    path('rooms/', views.getRooms),  # Get all rooms
    path('rooms/<str:pk>/', views.getRoom),  # Get a single room
]