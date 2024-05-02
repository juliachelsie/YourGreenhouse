from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Post
from django.http import HttpResponseRedirect
from .forms import CommentOnForm, ContactForm
from django.contrib import messages
from django.shortcuts import redirect


def get_index(request):
    return render(request, 'index.html')


def get_post(request):
    return render(request, 'post.html')


def get_contact(request):
    return render(request, 'contact.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created")
    template_name = 'post.html'
    paginate_by = 6


class Details(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = post.comment.filter(approved=True).order_by("-created")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "details.html",
            {
                "post": post,
                "comment": comment,
                "commented": False,
                "liked": liked,
                "comment_on_form": CommentOnForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = post.comment.filter(approved=True).order_by("-created")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_on_form = CommentOnForm(data=request.POST)
        if comment_on_form.is_valid():
            comment_on_form.instance.email = request.user.email
            comment_on_form.instance.name = request.user.username
            commenton = comment_on_form.save(commit=False)
            commenton.post = post
            commenton.save()
        else:
            comment_on_form = CommentOnForm()

        return render(
            request,
            "details.html",
            {
                "post": post,
                "comment": comment,
                "commented": True,
                "comment_on_form": comment_on_form,
                "liked": liked,
            },
        )


class Like(View):
    def post(self, request, slug,  *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        # Redirect to the details view with the correct slug parameter
        return redirect('details.html', slug=slug)


def contact_view(request):
    if request.method == 'POST':
        contactform = ContactForm(data=request.POST)
        if contactform.is_valid():
            contactform.save()
            messages.success(request, 'Message Sent!')
            return render(request, 'index.html')
    contactform = ContactForm()
    context = {'contactform': contactform}
    return render(request, 'contact.html', context)
