from django.urls import path
from . import views

app_name = 'post'


urlpatterns = [
    path('', views.new ,  name='new'),
    path('<int:pk>', views.edit ,  name='edit'),

]
