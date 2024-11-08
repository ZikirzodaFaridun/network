from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from .models import Post
from django import forms
from .models import CustomUser
from .models import Comment, Comment2, Comment5
from .models import Comment, Post  # Ensure Comment is imported
from django import forms
from .models import ChatMessage
from .models import Post, ImagePost, VideoPost
from .models import ShortsPost, Category
from django import forms
from .models import Announcement
from .models import TextPost, Comment3, Comment4

class TextPostForm(forms.ModelForm):
    class Meta:
        model = TextPost
        fields = ['content']  # Only the content field for text posts

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 20:
            raise forms.ValidationError("Content must be at least 20 characters.")
        if len(content) > 150:
            raise forms.ValidationError("Content must be at most 150 characters.")
        return content

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'image', 'video', 'phone_number']
    
    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)
        # Set all fields as required and add placeholders
        for field in self.fields.values():
            field.required = True
            field.widget.attrs.update({'placeholder': f'Enter {field.label.lower()}'})
        # Ensure the phone_number field is restricted to numeric input
        self.fields['phone_number'].widget.attrs.update({
            'type': 'tel',
            'pattern': '[0-9]+',
            'title': 'Enter a valid phone number with only numbers'
        })

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Type your message here...', 'rows': 3}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class CommentForm2(forms.ModelForm):
    class Meta:
        model = Comment2
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'Comment here...'}),
        }
class CommentForm3(forms.ModelForm):
    class Meta:
        model = Comment3
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'Comment here...'}),
        }
class CommentForm4(forms.ModelForm):
    class Meta:
        model = Comment4
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'Comment here...'}),
        }
class CommentForm5(forms.ModelForm):
    class Meta:
        model = Comment5
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'Comment here...'}),
        }
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'bio', 'profile_image', 'image2', 'gender', 'email', 'status']  # Include all editable fields

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-input'})
        self.fields['content'].widget.attrs.update({'class': 'form-input'})
        self.fields['category'].queryset = Category.objects.all()  # Get all categories


class ImagePostForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ['title', 'content', 'image', 'category']

    

class VideoPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    class Meta:
        model = VideoPost
        fields = ['title', 'content', 'video', 'category']

    def __init__(self, *args, **kwargs):
        super(VideoPostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-input'})
        self.fields['content'].widget.attrs.update({'class': 'form-input'})
        self.fields['video'].widget.attrs.update({'class': 'form-input'})

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_image', 'image2', 'gender', 'password', 'status']
class ShortsPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    class Meta:
        model = ShortsPost
        fields = ['content', 'video', 'category']

    def clean_video(self):
        video = self.cleaned_data.get('video')
        # Check if the video file size and duration is under 1 minute
        if video:
            # You may need a library like moviepy to check the duration
            import moviepy.editor as mp
            
            clip = mp.VideoFileClip(video.temporary_file_path())
            if clip.duration > 60:
                raise forms.ValidationError('Video must be less than 1 minute.')
        return video