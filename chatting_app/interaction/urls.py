from django.urls import path

from . import views
app_name = 'interaction'

urlpatterns = [
    path('', views.all_chats, name='all_chats'),
    path('chat/<int:pk>', views.chat_view, name='chat_page'),
    path('send_message/', views.create_message, name='create_message')
]