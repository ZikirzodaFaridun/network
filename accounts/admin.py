# admin.py
from django.contrib import admin
from .models import TextPost
from django.contrib import admin
from .models import (
    Announcement,
    BlockedUser,
    CustomUser,
    Profile,
    ChatMessage,
    Category,
    Post,
    ImagePost,
    VideoPost,
    ShortsPost,
    Like,
    Follow,
    Follow2,
    Comment,
)
from django.contrib import admin
from .models import FriendRequest

class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'created_at', 'status')
    list_filter = ('status',)
    search_fields = ('from_user__username', 'to_user__username')

admin.site.register(FriendRequest, FriendRequestAdmin)

admin.site.register(TextPost)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)

@admin.register(BlockedUser)
class BlockedUserAdmin(admin.ModelAdmin):
    list_display = ('blocker', 'blocked')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'timestamp')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'likes_count')  # Add likes_count to list display
    list_editable = ('likes_count',)
    

@admin.register(ImagePost)
class ImagePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')

@admin.register(VideoPost)
class VideoPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')

@admin.register(ShortsPost)
class ShortsPostAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'created_at')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'followed')

@admin.register(Follow2)
class Follow2Admin(admin.ModelAdmin):
    list_display = ('follower', 'followed')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')
