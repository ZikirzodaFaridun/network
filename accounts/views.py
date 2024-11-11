from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import CustomUser
from .forms import RegistrationForm
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from .models import Post, Follow
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import logout
from .models import Post, Comment
from .forms import CommentForm
from .models import ChatMessage
from .forms import ChatMessageForm
from django.contrib.auth import get_user_model  # Add this line
from django.db import models
from .models import CustomUser, Follow2
from .models import Post, Like
from .models import ChatMessage, BlockedUser
from .models import Post, ImagePost, VideoPost
from django.shortcuts import render, redirect
from .forms import PostForm, ImagePostForm, VideoPostForm, CommentForm2
from .models import Post, ImagePost, VideoPost,ShortsPost
from .forms import ShortsPostForm
from .models import VideoPost
from django.shortcuts import render, redirect
from .models import Category  # Adjust based on your app structure
from datetime import timedelta
from .models import Post, ImagePost, VideoPost, ShortsPost
from .models import Post, ImagePost, VideoPost, ShortsPost, Announcement
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Announcement, TextPost
from .forms import AnnouncementForm  # Assuming you'll create this form
from .forms import CommentForm3, CommentForm4, CommentForm5
from django.contrib import messages
from .models import FriendRequest
from django.urls import reverse
from django.http import HttpResponse

def index(request):
    return render("accounts/index.html)

@login_required
def inbox(request):
    received_requests = FriendRequest.objects.filter(to_user=request.user)
    sent_requests = FriendRequest.objects.filter(from_user=request.user)
    
    return render(request, 'accounts/inbox.html', {
        'received_requests': received_requests,
        'sent_requests': sent_requests,
    })

@login_required
def send_friend_request(request, user_id):
    to_user = get_object_or_404(CustomUser, id=user_id)
    
    # Check if a request already exists
    existing_request = FriendRequest.objects.filter(from_user=request.user, to_user=to_user).first()
    if not existing_request:
        FriendRequest.objects.create(from_user=request.user, to_user=to_user)
    
    return redirect(reverse('profile', kwargs={'username': to_user.username}))


@login_required
def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id, to_user=request.user)
    
    # Update status to 'accepted' and add users as friends
    friend_request.status = 'accepted'
    friend_request.save()
    
    request.user.friends.add(friend_request.from_user)
    friend_request.from_user.friends.add(request.user)
    
    return redirect('inbox')

@login_required
def decline_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id, to_user=request.user)
    
    # Update status to 'declined'
    friend_request.status = 'declined'
    friend_request.save()
    
    return redirect('inbox')

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(TextPost, id=post_id)
    if request.method == 'POST':
        form = CommentForm2(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user  # Associate the comment with the logged-in user
            comment.save()
            return redirect('text_post_list')  # Redirect back to the text post list
    return redirect('text_post_list') 

@login_required
def text_post_list(request):
    text_posts = TextPost.objects.prefetch_related('comments').order_by('-created_at')
    # Handle comment submission
    if request.method == 'POST':
        form = CommentForm2(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # Assign the current user
            comment.post = get_object_or_404(TextPost, id=request.POST.get('post_id'))
            comment.save()
            return redirect('text_post_list')  # Redirect to the same page after saving
    else:
        form = CommentForm2()

    return render(request, 'accounts/text_post_list.html', {
        'text_posts': text_posts,
        'form': form,
    })
@login_required
def image_post_list(request):
    image_posts = ImagePost.objects.all().order_by('-created_at')
    # Handle comment submission
    if request.method == 'POST':
        form = CommentForm3(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # Assign the current user
            comment.post = get_object_or_404(ImagePost, id=request.POST.get('post_id'))
            comment.save()
            return redirect('image_post_list')  # Redirect to the same page after saving
    else:
        form = CommentForm3()

    return render(request, 'accounts/image-post.html', {
        'text_posts': image_posts,
        'form': form,
    })

@login_required
def video_post_list(request):
    image_posts = VideoPost.objects.all().order_by('-created_at')
    # Handle comment submission
    if request.method == 'POST':
        form = CommentForm4(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # Assign the current user
            comment.post = get_object_or_404(VideoPost, id=request.POST.get('post_id'))
            comment.save()
            return redirect('video_post_list')  # Redirect to the same page after saving
    else:
        form = CommentForm4()

    return render(request, 'accounts/video-post.html', {
        'text_posts': image_posts,
        'form': form,
    })
@login_required
def shorts_post_list(request):
    image_posts = ShortsPost.objects.all().order_by('-created_at')
    # Handle comment submission
    if request.method == 'POST':
        form = CommentForm5(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # Assign the current user
            comment.post = get_object_or_404(ShortsPost, id=request.POST.get('post_id'))
            comment.save()
            return redirect('shorts_post_list')  # Redirect to the same page after saving
    else:
        form = CommentForm5()

    return render(request, 'accounts/shorts-post.html', {
        'text_posts': image_posts,
        'form': form,
    })

@login_required
def create_text_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        # Create a new TextPost; likes_count will default to 0
        post = TextPost(user=request.user, content=content)
        post.save()  # likes_count is set to default value (0)
        return redirect('text_post_list')
    return render(request, 'accounts/create_text_post.html')

class AnnouncementCreateView(CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'accounts/create_announcement.html'
    success_url = reverse_lazy('announcements')  # Redirect to the list of announcements after creating one

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current logged-in user
        return super().form_valid(form)

from django.views.generic import ListView
from .models import Announcement

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'accounts/announcements_list.html'  # Template file for displaying announcements
    context_object_name = 'announcements'
    ordering = ['-created_at'] 

def category_list(request):
    query = request.GET.get('q')
    categories = Category.objects.all()

    if query:
        categories = categories.filter(name__icontains=query)

    return render(request, 'accounts/category_list.html', {'categories': categories, 'query': query})

def get_started(request):
    return render(request, 'accounts/get_started.html')

def edit_image_post(request, pk):
    post = get_object_or_404(ImagePost, pk=pk)
    if post.author != request.user:
        return render("home")

    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')  # Change to your home URL
    else:
        form = ImagePostForm(instance=post)

    return render(request, 'accounts/edit_post.html', {'form': form, 'post_type': 'Image'})

def edit_video_post(request, pk):
    post = get_object_or_404(VideoPost, pk=pk)

    if post.author != request.user:
       return redirect('home')

    if request.method == 'POST':
        form = VideoPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')  # Change to your home URL
    else:
        form = VideoPostForm(instance=post)

    return render(request, 'accounts/edit_post.html', {'form': form, 'post_type': 'Video'})

def edit_shorts_post(request, pk):  # Keep the parameter as 'pk'
    post = get_object_or_404(ShortsPost, pk=pk)

    if post.author != request.user:
         return redirect('home')

    if request.method == 'POST':
        form = ShortsPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')  # Change to your home URL
    else:
        form = ShortsPostForm(instance=post)

    return render(request, 'accounts/edit_post.html', {'form': form, 'post_type': 'Shorts'})

def set_user_preferences(request):
    categories = Category.objects.all()  # Fetch all categories
    # Your existing logic here
    return render(request, 'accounts/set_preferences.html', {'categories': categories})



def create_shorts_post(request):
    if request.method == 'POST':
        form = ShortsPostForm(request.POST, request.FILES)
        if form.is_valid():
            shorts_post = form.save(commit=False)
            shorts_post.author = request.user
            shorts_post.save()
            return redirect('post_list')  # Redirect to the post list after saving
    else:
        form = ShortsPostForm()
    return render(request, 'accounts/create_shorts.html', {'form': form})


def posts_by_category(request, category_id):
    # Retrieve the category by ID
    category = Category.objects.get(id=category_id)
    
    # Filter all post types by the selected category
    posts = Post.objects.filter(
        ~Q(id__in=ImagePost.objects.values_list('id', flat=True)),
        ~Q(id__in=VideoPost.objects.values_list('id', flat=True)),
        ~Q(id__in=ShortsPost.objects.values_list('id', flat=True)),
        category=category
    ).order_by('-created_at')
    image_posts = ImagePost.objects.filter(category=category)
    video_posts = VideoPost.objects.filter(category=category)
    shorts_posts = ShortsPost.objects.filter(category=category)
    
    # Combine all posts into a single queryset-like list
    all_posts = list(posts) + list(image_posts) + list(video_posts) + list(shorts_posts)
    
    # Optionally, sort by a field like `created_at` if needed (assuming each model has this field)
    all_posts.sort(key=lambda x: x.created_at, reverse=True)

    return render(request, 'accounts/posts_by_category.html', {
        'category': category,
        'all_posts': all_posts,
    })

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            post = form.save(commit=False)  # Create a Post instance but don’t save it to the database yet
            post.author = request.user  # Set the author to the currently logged-in user
            post.save()  # Now save the instance to the database
            return redirect('post_list')  # Redirect to the post list after creating the post
    else:
        form = PostForm()
    
    return render(request, 'accounts/create_post.html', {'form': form})

def create_image_post(request):
    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            image_post = form.save(commit=False)  # Create the ImagePost instance but don’t save it to the database yet
            image_post.author = request.user  # Set the author to the current user
            image_post.save()  # Now save the instance to the database
            return redirect('home')  # Redirect to the post list after creating the post
    else:
        form = ImagePostForm()
    
    return render(request, 'accounts/create_image_post.html', {'form': form})

def create_video_post(request):
    if request.method == 'POST':
        form = VideoPostForm(request.POST, request.FILES)
        if form.is_valid():
            video_post = form.save(commit=False)
            video_post.author = request.user
            video_post.save()
            return redirect('post_list')  # Redirect after successful upload
    else:
        form = VideoPostForm()

    return render(request, 'accounts/create_video_post.html', {'form': form})


User = get_user_model()
@login_required
def delete_chat(request, user_id):
    recipient = get_object_or_404(User, id=user_id)
    # Delete all messages between the logged-in user and the recipient
    ChatMessage.objects.filter(
        (Q(sender=request.user) & Q(recipient=recipient)) |
        (Q(sender=recipient) & Q(recipient=request.user))
    ).delete()
    return redirect('chats_users')
@login_required
def chats_users(request):
    chat_partners_ids = ChatMessage.objects.filter(
        Q(sender=request.user) | Q(recipient=request.user)
    ).values_list('sender', 'recipient').distinct()

    chat_partners_ids = {user_id for user_pair in chat_partners_ids for user_id in user_pair if user_id != request.user.id}
    
    # Get blocked users
    blocked_ids = BlockedUser.objects.filter(blocker=request.user).values_list('blocked', flat=True)
    
    # Exclude blocked users from chat partners
    chat_partners = User.objects.filter(id__in=chat_partners_ids).exclude(id__in=blocked_ids)

    return render(request, 'accounts/chats_users.html', {'users': chat_partners})

@login_required
def block_chat(request, user_id):
    recipient = get_object_or_404(User, id=user_id)
    # Block the user
    BlockedUser.objects.get_or_create(blocker=request.user, blocked=recipient)
    
    # Delete all messages between the logged-in user and the blocked recipient
    ChatMessage.objects.filter(
        (Q(sender=request.user) & Q(recipient=recipient)) |
        (Q(sender=recipient) & Q(recipient=request.user))
    ).delete()
    
    return redirect('chats_users')

@login_required
def chat_view(request, user_id):
    recipient = get_object_or_404(User, id=user_id)
    
    # Check if the recipient is blocked
    if BlockedUser.objects.filter(blocker=request.user, blocked=recipient).exists():
        return render(request, 'accounts/chat_blocked.html', {'recipient': recipient})
    
    # Get all messages between the logged-in user and the recipient
    messages = ChatMessage.objects.filter(
        (Q(sender=request.user) & Q(recipient=recipient)) |
        (Q(sender=recipient) & Q(recipient=request.user))
    ).order_by('timestamp')

    if request.method == 'POST':
        form = ChatMessageForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.sender = request.user
            chat_message.recipient = recipient
            chat_message.save()
            return redirect('chat_view', user_id=user_id)

    else:
        form = ChatMessageForm()

    return render(request, 'accounts/chat.html', {
        'recipient': recipient,
        'messages': messages,
        'form': form,
        'user_image': request.user.profile_image.url if request.user.profile_image else None,
        'recipient_image': recipient.profile_image.url if recipient.profile_image else None,
    })
@login_required
def toggle_follow2(request, username):
    user_to_follow = get_object_or_404(CustomUser, username=username)

    # Check if the user already follows this profile user with Follow2
    follow2, created = Follow2.objects.get_or_create(follower=request.user, followed=user_to_follow)
    
    if not created:
        # If the Follow2 relationship already exists, delete it (Unfollow2)
        follow2.delete()
    # If created, then this is a new follow action
    
    return redirect('profile', username=username)
@login_required
def follow_user2(request, username):
    user_to_follow = get_object_or_404(CustomUser, username=username)
    if request.user != user_to_follow:
        Follow2.objects.get_or_create(follower=request.user, followed=user_to_follow)
    return redirect('profile', username=username)

@login_required
def unfollow_user2(request, username):
    user_to_unfollow = get_object_or_404(CustomUser, username=username)
    Follow2.objects.filter(follower=request.user, followed=user_to_unfollow).delete()
    return redirect('profile', username=username)

User = get_user_model()
@login_required
def chat_view(request, user_id):
    recipient = get_object_or_404(User, id=user_id)
    
    # Check if the recipient is blocked
    if BlockedUser.objects.filter(blocker=request.user, blocked=recipient).exists():
        return render(request, 'accounts/chat_blocked.html', {'recipient': recipient})
    
    # Get all messages between the logged-in user and the recipient
    messages = ChatMessage.objects.filter(
        (Q(sender=request.user) & Q(recipient=recipient)) |
        (Q(sender=recipient) & Q(recipient=request.user))
    ).order_by('timestamp')
    
    # Mark messages as seen when loaded

    if request.method == 'POST':
        form = ChatMessageForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.sender = request.user
            chat_message.recipient = recipient
            chat_message.save()
            return redirect('chat_view', user_id=user_id)

    else:
        form = ChatMessageForm()

    return render(request, 'accounts/chat.html', {
        'recipient': recipient,
        'messages': messages,
        'form': form,
        'user_image': request.user.profile_image.url if request.user.profile_image else None,
        'recipient_image': recipient.profile_image.url if recipient.profile_image else None,
    })

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home after logout

@login_required
def edit_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    # Check if the user is trying to edit their own profile
    if request.user != user:
        return redirect('edit_profile', user_id=request.user.id)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a relevant page after saving
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        Follow.objects.get_or_create(follower=request.user, followed=user_to_follow)
    return redirect('profile', username=user_to_follow.username)

@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        Follow.objects.filter(follower=request.user, followed=user_to_unfollow).delete()
    return redirect('profile', username=user_to_unfollow.username)


@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    posts = Post.objects.filter(author=user)
    all_posts = Post.objects.filter(
    ~Q(id__in=ImagePost.objects.values_list('post_ptr_id', flat=True)),
    ~Q(id__in=VideoPost.objects.values_list('post_ptr_id', flat=True)),
    ~Q(id__in=ShortsPost.objects.values_list('id', flat=True)),
        author=request.user,

).order_by('-created_at')
    
    image_posts = ImagePost.objects.filter(author=user)
    video_posts = VideoPost.objects.filter(author=user)
    shorts_posts = ShortsPost.objects.filter(author=user)
    sent_requests = FriendRequest.objects.filter(from_user=request.user)

    # Check if the current user has sent a friend request to this user
    request_sent = FriendRequest.objects.filter(from_user=request.user, to_user=user).first()

    # Check follow status for both Follow and Follow2 models
    is_following = Follow.objects.filter(follower=request.user, followed=user).exists()
    is_following2 = Follow2.objects.filter(follower=request.user, followed=user).exists()

    is_self = user == request.user

    # Follow model 1 counts and lists
    followers_count = Follow.objects.filter(followed=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    followers_list = Follow.objects.filter(followed=user).select_related('follower')
    following_list = Follow.objects.filter(follower=user).select_related('followed')

    # Follow2 model counts and lists
    followers_count2 = Follow2.objects.filter(followed=user).count()
    following_count2 = Follow2.objects.filter(follower=user).count()
    followers2_list = Follow2.objects.filter(followed=user).select_related('follower')
    following2_list = Follow2.objects.filter(follower=user).select_related('followed')

    context = {
        'user': user,
        'posts': posts,
        'is_following': is_following,
        'is_following2': is_following2,
        'is_self': is_self,
        'followers_count': followers_count,
        'following_count': following_count,
        'followers_list': followers_list,
        'following_list': following_list,
        'followers_count2': followers_count2,
        'following_count2': following_count2,
        'followers2_list': followers2_list,
        'following2_list': following2_list,
        'sent_requests': sent_requests,
        'request_sent': request_sent,
        'image_posts':image_posts,
        'video_posts':video_posts,
        'shorts_posts':shorts_posts
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the current user
            post.save()
            return redirect('home')  # Redirect to home after saving
    else:
        form = PostForm()
    return render(request, 'accounts/add_post.html', {'form': form})



@login_required
def user_list(request):
    query = request.GET.get('search', '')  # Get the search query from the GET request
    users = CustomUser.objects.exclude(id=request.user.id)  # Exclude the logged-in user

    if query:
        # Filter users by username (or other fields as necessary)
        users = users.filter(username__icontains=query)

    return render(request, 'accounts/user_list.html', {'users': users, 'query': query})

def post_list(request):
    posts2 = TextPost.objects.all()
    # Retrieve all posts
    posts = Post.objects.filter(
    imagepost__isnull=True,
    videopost__isnull=True
).order_by('-created_at')

    query = request.GET.get('q')
    image_posts = ImagePost.objects.all()
    video_posts = VideoPost.objects.all()

    comment_form = CommentForm()
    viewed_posts = set(request.session.get('viewed_posts', []))
    shorts_posts = ShortsPost.objects.all()
    # Increment view count for posts that haven't been viewed by the user

    comment_form = CommentForm()
    viewed_posts = set(request.session.get('viewed_posts', []))

    # Increment view count for posts that haven't been viewed by the user
    for post in posts:
        if request.user.is_authenticated and request.user != post.author and post.id not in viewed_posts:
            post.views += 1  # Increment the view count
            post.save()  # Save the updated view count
            viewed_posts.add(post.id)  # Track the viewed post

    request.session['viewed_posts'] = list(viewed_posts)  # Store viewed posts in session

    # Handle comment submission
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post_id = request.POST.get('post_id')  # Get the post ID
            comment.save()
            return redirect('post_list')  # Redirect to the same page after saving
    if query:
        posts = posts.filter(content__icontains=query)
    # Render the posts to the template
    return render(request, 'accounts/post_list.html', {
        'posts': posts,
        'image_posts': image_posts,
        'video_posts': video_posts,
        'comment_form': comment_form,
        'shorts_posts': shorts_posts,
        'query': query,
        'posts2':posts2
    })


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')  # Adjust to your login page name
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.get_or_create(user=request.user, post=post)
    return redirect('post_list')

@login_required
def unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like_instance = Like.objects.filter(user=request.user, post=post)
    if like_instance.exists():
        like_instance.delete()
    return redirect('post_list')

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, redirect
from .models import TextPost, Like


from django.contrib import messages
@login_required
def toggle_like_text_post(request, post_id):
    post = get_object_or_404(TextPost, id=post_id)
    
    # Check if the user has already liked the post
    existing_like = Like.objects.filter(user=request.user, post=post).first()
    
    if existing_like:
        # If the user already liked the post, remove the like
        existing_like.delete()
        post.likes_count -= 1  # Decrement likes count
        post.save()
        liked = False  # Indicate that the post is no longer liked
    else:
        # If the user hasn't liked the post yet, create a new like
        Like.objects.create(user=request.user, post=post)
        post.likes_count += 1  # Increment likes count
        post.save()
        liked = True  # Indicate that the post is liked

    return redirect('text_post_list') 
@login_required
def toggle_like_image_post(request, pk):
    post = get_object_or_404(ImagePost, pk=pk)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)  # Unlike the post
    else:
        post.likes.add(request.user)  # Like the post

    post.likes_count = post.likes.count()
    post.save()

    return redirect('image_post_list') 

@login_required
def toggle_like_video_post(request, pk):
    post = get_object_or_404(VideoPost, pk=pk)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)  # Unlike the post
    else:
        post.likes.add(request.user)  # Like the post

    post.likes_count = post.likes.count()
    post.save()

    return redirect('video_post_list')

@login_required
def toggle_like_shorts_post(request, pk):
    post = get_object_or_404(ShortsPost, pk=pk)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)  # Unlike the post
    else:
        post.likes.add(request.user)  # Like the post

    post.likes_count = post.likes.count()
    post.save()

    return redirect('shorts_post_list')

@login_required
def like_text_post(request, post_id):
    post = get_object_or_404(TextPost, id=post_id)
    
    existing_like = Like.objects.filter(user=request.user, post=post).first()
    
    if not existing_like:
        Like.objects.create(user=request.user, post=post)
        post.likes_count += 1
        post.save()
    else:
        messages.warning(request, 'You have already liked this post.')  # Inform the user

    return redirect('text_post_list')  # Redirect to your text post list

@login_required
def unlike_text_post(request, post_id):
    post = get_object_or_404(TextPost, id=post_id)
    # Find the like instance
    like_instance = Like.objects.filter(user=request.user, post=post)
    if like_instance.exists():
        like_instance.delete()  # Remove the like
        # Decrement the likes count
        post.likes_count -= 1
        post.save()
    return redirect('text_post_list')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/login.html')

@login_required
def home(request):
    user = request.user
    all_posts = Post.objects.filter(
    ~Q(id__in=ImagePost.objects.values_list('post_ptr_id', flat=True)),
    ~Q(id__in=VideoPost.objects.values_list('post_ptr_id', flat=True)),
    ~Q(id__in=ShortsPost.objects.values_list('id', flat=True)),
        author=request.user,

).order_by('-created_at')
    text_posts = TextPost.objects.filter(user=request.user).prefetch_related('comments').order_by('-created_at')
    # Handle comment submission
    if request.method == 'POST':
        form = CommentForm2(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # Assign the current user
            comment.post = get_object_or_404(TextPost, id=request.POST.get('post_id'))
            comment.save()
            return redirect('text_post_list')  # Redirect to the same page after saving
    else:
        form = CommentForm2()
    
    image_posts = ImagePost.objects.filter(author=user)
    video_posts = VideoPost.objects.filter(author=user)
    shorts_posts = ShortsPost.objects.filter(author=user)
    # Get the users followed by the logged-in user
    following_users = Follow.objects.filter(follower=request.user).select_related('followed')
    # Get the users following the logged-in user
    followers_users = Follow.objects.filter(followed=request.user).select_related('follower')

    # Get the counts
    following_count = following_users.count()
    followers_count = followers_users.count()
    following_users2 = Follow2.objects.filter(follower=request.user).select_related('followed')
    # Get the users following the logged-in user
    followers_users2 = Follow2.objects.filter(followed=request.user).select_related('follower')

    # Get the counts
    following_count2 = following_users2.count()
    followers_count2 = followers_users2.count()


    context = {
        'following_users': following_users,
        'followers_users': followers_users,
        'following_count': following_count,
        'followers_count': followers_count,
        'following_users2': following_users2,
        'followers_users2': followers_users2,
        'following_count2': following_count2,
        'followers_count2': followers_count2,
        'image_posts': image_posts,
        'video_posts': video_posts,
        'shorts_posts': shorts_posts,
        'all_posts': all_posts,
        'text_posts': text_posts,
        'form': form,
    }
    return render(request, 'accounts/home.html', context)

from django.http import HttpResponseForbidden

@login_required
def edit_post(request, post_id):
    # Retrieve the post instance
    post = get_object_or_404(Post, id=post_id)

    # Ownership check: Ensure that only the post's creator can edit it
    if post.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        # Bind the form to the post instance for editing
        form = PostForm(request.POST, request.FILES, instance=post)
        
        if form.is_valid():
            form.save()  # Save the post with updated data
            return redirect('home')  # Redirect to home or another page after saving
    else:
        # Initialize form with the existing post data for GET requests
        form = PostForm(instance=post)

    return render(request, 'accounts/edit_post.html', {'form': form, 'post': post})
