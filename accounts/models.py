from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.db import models

class FriendRequest(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_requests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='sent')

    def __str__(self):
        return f"{self.from_user} to {self.to_user} - {self.status}"


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='announcement_images/', blank=True, null=True)
    video = models.FileField(upload_to='announcement_videos/', blank=True, null=True)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\d{10,15}$', 'Enter a valid phone number with 10-15 digits')],
        blank=True,  # Allow blank for now
        null=True    # Allow null for now
    )

    def __str__(self):
        return self.title
    
class BlockedUser(models.Model):
    blocker = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blocked_users', on_delete=models.CASCADE)
    blocked = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blocked_by', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.blocker} blocked {self.blocked}"
# Define CustomUser model
class CustomUser(AbstractUser):
    friends = models.ManyToManyField("self", blank=True, symmetrical=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images2/', blank=True, null=True)
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    STATUS_CHOICES = [
        ('O', 'Open'),
        ('C', 'Close')
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.username

# Profile model
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='profile_friends', blank=True)  # Unique related_name

    def __str__(self):
        return self.user.username

# ChatMessage model
class ChatMessage(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.sender.username} to {self.recipient.username}: {self.message[:20]}"

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class TextPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes_count = models.PositiveIntegerField(default=0)


# Post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_image_posts', blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=1  # Assuming "Uncategorized" has ID 1
    )  # Link to category  # Link to category

    def __str__(self):
        return self.title

class ImagePost(Post):
    image = models.ImageField(upload_to='posts_images/', blank=True, null=True)
    

class VideoPost(Post):
    video = models.FileField(upload_to='posts_videos/', blank=True, null=True)

    
class ShortsPost(models.Model):
    content = models.CharField(max_length=150, default="I m post shorts")
    video = models.FileField(upload_to='shorts_videos/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)  # Add category
    likes_count = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_shorts_posts', blank=True)

    def __str__(self):
        return f'Short by {self.author.username} at {self.created_at}'
    
class Comment2(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Reference to user
    post = models.ForeignKey(TextPost, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)  # Reference to the post
    content = models.TextField()  # Field for the comment content
    created_at = models.DateTimeField(auto_now_add=True)
class Comment3(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Reference to user
    post = models.ForeignKey(ImagePost, related_name='comments3', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()  # Field for the comment content
    created_at = models.DateTimeField(auto_now_add=True)
class Comment4(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Reference to user
    post = models.ForeignKey(VideoPost, related_name='comments4', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()  # Field for the comment content
    created_at = models.DateTimeField(auto_now_add=True)
class Comment5(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Reference to user
    post = models.ForeignKey(ShortsPost, related_name='comments5', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()  # Field for the comment content
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('TextPost', related_name='likes', on_delete=models.CASCADE)  # Ensure it's related to TextPost

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} likes {self.post.content[:20]}"

    class Meta:
        unique_together = ('user', 'post')   
    
# Follow model
class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'followed')

    def __str__(self):
        return f"{self.follower} follows {self.followed}"
    
class Follow2(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followed_users', on_delete=models.CASCADE)
    followed = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers2', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.follower} follows {self.followed}"

# Comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username}'
