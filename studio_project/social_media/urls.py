from django.urls import path
from social_media import views

app_name = 'social_media'

urlpatterns = [
    path('connect/', views.connect_to_social_media, name='connect'),
    path('facebook/callback/', views.facebook_callback, name='facebook_callback'),
]