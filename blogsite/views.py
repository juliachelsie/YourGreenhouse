from django.shortcuts import render
from django.views import generic
from .models import Post

def get_index(request):
    return render(request, 'index.html')

def get_post(request):
    return render(request, 'post.html')


class viewList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created')
    template_name = 'post.html'
    paginate_by = 6

