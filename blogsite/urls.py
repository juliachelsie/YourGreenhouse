from . import views 
from django.urls import path

urlpatterns = [
    path('', views.viewList.as_view(), name='home')
]