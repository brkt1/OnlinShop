from django.urls import path
from . import views

app_name = 'dashbordapp'


urlpatterns = [
    path('', views.dashboard ,  name='dashboard'),

]
