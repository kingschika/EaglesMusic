from django import forms
from studio_app import models
from .models import  Music, Video, Profile, AuthorizationPin
from django.contrib.auth.models import User
from .models import ComedyPost
from .models import MusicAuthorizationPin


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ('title', 'artist', 'audio_file')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter song title'}),
            'artist': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Artist name'}),
            'audio_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class MusicAuthorizationForm(forms.ModelForm):
    authorization = forms.CharField(label='Authorization Pin', widget=forms.PasswordInput)
    authorization2 = forms.CharField(label='Repeat Authorization Pin', widget=forms.PasswordInput)

    class Meta:
        model = MusicAuthorizationPin
        fields = ('authorization_pin',)

    def clean_authorization2(self):
        cd = self.cleaned_data
        if cd['authorization'] != cd['authorization2']:
            raise forms.ValidationError('Authorization pins do not match.')
        if cd['authorization'] != 'fadiya1234':
            raise forms.ValidationError('Invalid authorization pin.')
        return cd['authorization2']


        
class VideoForm(forms.ModelForm):
    class Meta:
           model = Video
           fields = ['id', 'title', 'artist', 'video_file']
           
           

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture', 'role', 'favorite_songs', 'favorite_artists', 'favorite_videos']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'favorite_songs': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'favorite_artists': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'favorite_videos': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
      

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']
    
    
    
class VideoAuthorizationForm(forms.ModelForm):
    authorization = forms.CharField(label='Authorization Pin', widget=forms.PasswordInput)
    authorization2 = forms.CharField(label='Repeat Authorization Pin', widget=forms.PasswordInput)

    class Meta:
        model = AuthorizationPin
        fields = ('authorization_pin',)

    def clean_authorization2(self):
        cd = self.cleaned_data
        if cd.get('authorization') != cd.get('authorization2'):
            raise forms.ValidationError('Authorization pins do not match.')
        # Optional: verify against model’s default pin
        stored_pin = getattr(AuthorizationPin.objects.first(), 'authorization_pin', 'fadiya1234')
        if cd.get('authorization') != stored_pin:
            raise forms.ValidationError('Invalid authorization pin.')
        return cd['authorization2']
     
   

    
    
        
   

class ComedyPostForm(forms.ModelForm):
    class Meta:
        model = ComedyPost
        fields = ('title', 'content', 'image', 'video', 'audio')
    