from django.contrib import admin
from blogsite import views as contact_view
from . import views
from django.urls import path
from .views import Details

urlpatterns = [
    path('post.html', views.PostList.as_view(), name='post.html'),
    path('', views.get_index, name='home'),
    path('post.html', views.get_post, name='post.html'),
    path('details/<slug:slug>/', Details.as_view(), name='details.html'),
    path('like/<slug:slug>', views.Like.as_view(), name='like'),
    path('contact.html', views.contact_view, name='contact.html'),

]
