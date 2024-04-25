from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    updated = models.DateTimeField(auto_now=True)
    chosen_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, blank=True, related_name="user_likes")

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def likes_number(self):
        return self.likes.count()


class CommentOn(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                            related_name="comment")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    body = models.TextField()

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    about = models.TextField()

    def __str__(self):
        return self.email
