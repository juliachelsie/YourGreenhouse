import unittest    
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.exceptions import PermissionDenied
from blogsite.models import Post, CommentOn, Contact
from blogsite.views import Like, Details
from blogsite.forms import CommentOnForm, ContactForm

    # MODELS.PY

    # Test Post Class in models.py.

class PostModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        cls.user = User.objects.create_user(username='test_user', password='password')

    def setUp(self):
        # Create a post
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            writer=self.user,
            content='Test content',
            excerpt='Test excerpt',
            status=0
        )

    def test_post_creation(self):
        """Test that a post is created correctly"""
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.slug, 'test-post')
        self.assertEqual(self.post.writer, self.user)
        self.assertEqual(self.post.content, 'Test content')
        self.assertEqual(self.post.excerpt, 'Test excerpt')
        self.assertEqual(self.post.status, 0)

    def test_str_representation(self):
        """Test the string representation of a post"""
        self.assertEqual(str(self.post), 'Test Post')

    def test_likes_number(self):
        """Test the number of likes for a post"""
        # Initially, the post should have no likes
        self.assertEqual(self.post.likes_number(), 0)

        # Add a like
        user_liking_post = User.objects.create_user(username='liking_user', password='password')
        self.post.likes.add(user_liking_post)

        # The number of likes should now be 1
        self.assertEqual(self.post.likes_number(), 1)


    # Test for CommentOn Class in models.py.

class CommentOnModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for testing
        cls.user = User.objects.create_user(username='test_user', email='test@example.com', password='password')
        # Create a post for testing
        cls.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            writer_id=1,  # Replace with an existing user ID
            content='Test content',
            excerpt='Test excerpt',
            status=0
        )

    def setUp(self):
        # Create a comment
        self.comment = CommentOn.objects.create(
            post=self.post,
            name='Test User',
            email='test@example.com',
            body='Test comment body'
        )

    def test_comment_creation(self):
        """Test that a comment is created correctly"""
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.name, 'Test User')
        self.assertEqual(self.comment.email, 'test@example.com')
        self.assertEqual(self.comment.body, 'Test comment body')
        self.assertFalse(self.comment.approved)

    def test_str_representation(self):
        """Test the string representation of a comment"""
        expected_string = f"Comment Test comment body by Test User"
        self.assertEqual(str(self.comment), expected_string)

    def test_ordering(self):
        """Test the ordering of comments"""
        # Create more comments with different timestamps
        comment1 = CommentOn.objects.create(
            post=self.post,
            name='User 1',
            email='user1@example.com',
            body='Comment 1',
            created='2024-04-30 12:00:00'
        )
        comment2 = CommentOn.objects.create(
            post=self.post,
            name='User 2',
            email='user2@example.com',
            body='Comment 2',
            created='2024-04-30 12:30:00'
        )

        # Retrieve comments ordered by creation time
        ordered_comments = CommentOn.objects.all()

        # Ensure comments are ordered correctly
        self.assertEqual(ordered_comments[0], self.comment)
        self.assertEqual(ordered_comments[1], comment1)
        self.assertEqual(ordered_comments[2], comment2)

    # Test for Contact Class in models.py.

class ContactModelTestCase(TestCase):
    def test_contact_creation(self):
        """Test that a contact is created correctly"""
        contact = Contact.objects.create(
            name='Luke Swanson',
            subject='Test Subject',
            email='luke@example.com',
            about='Test message'
        )
        self.assertEqual(contact.name, 'Luke Swanson')
        self.assertEqual(contact.subject, 'Test Subject')
        self.assertEqual(contact.email, 'luke@example.com')
        self.assertEqual(contact.about, 'Test message')

    def test_str_representation(self):
        """Test the string representation of a contact"""
        contact = Contact.objects.create(
            name='Karen Leek',
            subject='Another Subject',
            email='karen@example.com',
            about='Another test message'
        )
        self.assertEqual(str(contact), 'karen@example.com')

    # VIEWS.PY

    # Test for Like Class from views.py.

class LikeViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(username='test_user', email='test@example.com', password='password')

        # Create a test post
        cls.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            writer=cls.user,
            content='Test content',
            excerpt='Test excerpt',
            status=1  # Assuming status=1 indicates a published post
        )

    def setUp(self):
        self.factory = RequestFactory()

    def test_post_like(self):
    # Simulate a POST request to like the post
        request = self.factory.post(reverse('like', kwargs={'slug': 'test-post'}))
        request.user = self.user  # Set the request user
        response = Like.as_view()(request, slug='test-post')

        # Check if the post is liked by the user
        self.assertTrue(self.post.likes.filter(id=self.user.id).exists())

        # Check if the response redirects to the correct URL
        self.assertEqual(response.status_code, 302)  # 302 is the status code for redirection
        self.assertEqual(response.url, reverse('details', kwargs={'slug': 'test-post'}))

    def test_post_unlike(self):
        """Test unliking a post"""
        # Like the post first
        self.post.likes.add(self.user)

        # Simulate a POST request to unlike the post
        request = self.factory.post(reverse('like', kwargs={'slug': 'test-post'}))
        request.user = self.user  # Set the request user
        response = Like.as_view()(request, slug='test-post')

        # Check if the post is unliked by the user
        self.assertFalse(self.post.likes.filter(id=self.user.id).exists())

        # Check if the response redirects to the correct URL
        self.assertEqual(response.status_code, 302)  # 302 is the status code for redirection
        self.assertEqual(response.url, reverse('details', kwargs={'slug': 'test-post'}))

    # Test for Details Class from views.py

class DetailsViewTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Create a test post
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            writer=self.user,
            content='Test content',
            status=1,
            created=timezone.now()  # Use timezone.now() to set the created field
    )

    # FORMS.PY

    # Test for CommentOnForm from forms.py.

class TestCommentOnForm(TestCase):
    def test_valid_form(self):
        form_data = {'body': 'Test comment'}
        form = CommentOnForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        form = CommentOnForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'body': ['This field is required.']})

    def test_max_length(self):
        max_length = CommentOn._meta.get_field('body').max_length
        form_data = {'body': 'a' * (max_length + 1)}  # Exceed max length
        form = CommentOnForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'body': [f'Ensure this value has at most {max_length} characters (it has {max_length + 1}).']})

    # Test for ContactForm from forms.py.

class TestContactForm(TestCase):
    def test_valid_form(self):
        form_data = {
            'name': 'Test User',
            'subject': 'Test Subject',
            'email': 'test@example.com',
            'about': 'Test About'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_required_fields(self):
        form = ContactForm(data={})  # Empty data dictionary
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('subject', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('about', form.errors)