from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginPage, name='login'),  # Login page
    path('logout/', views.logoutUser, name='logout'),  # Login page
    path('register/', views.registerPage, name='register'),

    

    path('', views.home, name='home'),  # Home page
    path('room/<str:pk>/', views.room, name='room'),  # Room page
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),  # User profile page

    path('create-room/', views.createRoom, name='create-room'),  # Create room page
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),  # Update room page
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),  # Delete room page
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),  # Delete room page

]