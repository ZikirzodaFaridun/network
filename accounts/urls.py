# accounts/urls.py

from django.urls import path
from . import views
from .views import register, login_view, home, user_list, add_post, post_list, profile, logout_view, edit_profile,follow_user, unfollow_user, delete_chat
from .views import chat_view, chats_users, block_chat, edit_post, create_shorts_post
from .views import category_list, edit_shorts_post, create_text_post
from .views import AnnouncementCreateView, AnnouncementListView
from .views import text_post_list, create_text_post  # Import the new view
from .views import like_text_post, unlike_text_post
from .views import toggle_like_text_post, add_comment, toggle_like_image_post # Import the view

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('user_list/', user_list, name='user_list'),
    path('add_post/', add_post, name='add_post'),
    path('post_list/', post_list, name='post_list'),
    path('profile/<str:username>/', profile, name='profile'),
    path('profile/<str:username>/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),  # Add this line
    path('edit_profile/<int:user_id>/', edit_profile, name='edit_profile'),
    path('chat/<int:user_id>/', chat_view, name='chat_view'),
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
    path('profile/<str:username>/toggle_follow2/', views.toggle_follow2, name='toggle_follow2'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('post/<int:post_id>/unlike/', views.unlike_post, name='unlike_post'),
    path('chats/', chats_users, name='chats_users'),
    path('delete_chat/<int:user_id>/', delete_chat, name='delete_chat'),
    path('block_chat/<int:user_id>/', block_chat, name='block_chat'),
    path('chat/<int:user_id>/', chat_view, name='chat_view'),
    path('edit-post/<int:post_id>/', edit_post, name='edit_post'),  # URL for editing posts
    path('create/', views.create_post, name='create_post'),
    path('create/image/', views.create_image_post, name='create_image_post'),
    path('create/video/', views.create_video_post, name='create_video_post'),
    path('create/shorts/', create_shorts_post, name='create_shorts_post'),
    path('edit/image/<int:pk>/', views.edit_image_post, name='edit_image_post'),
    path('edit/video/<int:pk>/', views.edit_video_post, name='edit_video_post'),
    path('edit/shorts/<int:pk>/', edit_shorts_post, name='edit_shorts_post'),
    path('get-started/', views.get_started, name='get_started'),
    path('categories/', category_list, name='category_list'),
    path('categories/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('announcements/', AnnouncementListView.as_view(), name='announcements_list'),
    path('announcements/create/', AnnouncementCreateView.as_view(), name='create_announcement'),
    path('create-text-post/', create_text_post, name='create_text_post'),
    path('text-posts/', text_post_list, name='text_post_list'),  # URL for the text post list
    path('image-posts/', views.image_post_list, name='image_post_list'),  # URL for the text post list
    path('video-posts/', views.video_post_list, name='video_post_list'),
    path('shorts-posts/', views.shorts_post_list, name='shorts_post_list'),
    path('text-post/<int:post_id>/like/', like_text_post, name='like_text_post'),
    path('text-post/<int:post_id>/unlike/', unlike_text_post, name='unlike_text_post'),
    path('toggle-like-text-post/<int:post_id>/', toggle_like_text_post, name='toggle_like_text_post'),
    path('toggle-like-image-post/<int:pk>/', views.toggle_like_image_post, name='toggle-like-image-post'),
    path('toggle-like-video-post/<int:pk>/', views.toggle_like_video_post, name='toggle_like_video_post'),
    path('toggle-like-shorts-post/<int:pk>/', views.toggle_like_shorts_post, name='toggle_like_shorts_post'),
    path('send-friend-request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
    path('inbox/', views.inbox, name='inbox'),
    path('accept-friend-request/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('decline-friend-request/<int:request_id>/', views.decline_friend_request, name='decline_friend_request'),
]
