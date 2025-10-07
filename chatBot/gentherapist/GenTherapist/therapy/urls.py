"""
URL Configuration for therapy app
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_home, name='chat-home'),
    path('api/send-message/', views.send_message, name='send-message'),
    path('api/clear-conversation/', views.clear_conversation, name='clear-conversation'),
]
