from . import views 
from django.urls import path

urlpatterns = [
    path('post.html', views.viewList.as_view(), name=''),
    path('', views.get_index, name='home'),
    path('post.html', views.get_post, name='post.html')

]