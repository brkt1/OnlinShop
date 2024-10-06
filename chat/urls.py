from django.urls import path
from . import views

app_name = 'chat'  # Define the namespace here

urlpatterns = [
    path('start/<int:item_id>/', views.start_chat, name='start_chat'),
    path('<int:chat_id>/', views.chat_detail, name='chat_detail'),
]