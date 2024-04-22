from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentOnForm

def get_index(request):
    return render(request, 'index.html')


def get_post(request):
    return render(request, 'post.html')

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created')
    template_name = 'post.html'
    paginate_by = 6


class Details(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = post.comment.filter(approved=True).order_by('created')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "details.html",
            {
                "post":post,
                "comment": comment,
                "commented": False,
                "liked": liked,
                "comment_on_form" : CommentOnForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = post.comment.filter(approved=True).order_by('created')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_on_form = CommentOnForm(data=request.POST)

        if comment_on_form.is_valid():
            comment_on_form.instance.email = request.user.email
            comment_on_form.instance.name = request.user.username
            comment = comment_on_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_on_form = CommentOnForm()


        return render(
            request,
            "details.html",
            {
                "post":post,
                "comment": comment,
                "commented": True,
                "liked": liked,
                "comment_on_form" : CommentOnForm()
            },
        )

