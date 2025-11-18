from django.shortcuts import render

# Create your views here.

import requests
from django.shortcuts import redirect
from .models import SocialMedia

def connect_to_social_media(request):
    # Facebook
    facebook_app_id = 'YOUR_APP_ID'
    facebook_app_secret = 'YOUR_APP_SECRET'
    facebook_redirect_url = 'http://localhost:8000/social_media/facebook/callback'
    facebook_url = f'https://www.facebook.com/v13.0/dialog/oauth?client_id={facebook_app_id}&redirect_url={facebook_redirect_url}&scope=publish_to_groups,publish_stream'
    return redirect(facebook_url)

def facebook_callback(request):
    code = request.GET.get('code')
    # Get access token
    access_token_url = f'https://graph.facebook.com/v13.0/oauth/access_token?client_id=YOUR_APP_ID&redirect_uri=http://localhost:8000/social_media/facebook/callback&client_secret=YOUR_APP_SECRET&code={code}'
    response = requests.get(access_token_url)
    access_token = response.json()['access_token']
    # Save access token
    social_media = SocialMedia.objects.create(platform='Facebook', access_token=access_token)
    return redirect('studio_app:index')