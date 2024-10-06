from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings 
from django.conf.urls.static import static
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail,  name='detail'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('seller-chats/', views.seller_chats, name='seller_chats'),  # Seller's chats list

    path('delete/ <int:pk>',views.delet_item , name='delete'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)