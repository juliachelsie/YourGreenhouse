from django.contrib import admin
from django.urls import path, include
from blogsite.views import get_index, get_post, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_index, name='get_index'),
    path('', get_post, name='get_post'),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blogsite.urls'), name='blogsite_urls'),
    path('accounts/', include('allauth.urls')),
    path('contact.html', contact_view, name='contact.html'),
]
