from django.db import models
from django.contrib.auth.models import User


# ------------------------
# Artist Model
# ------------------------
class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='artists/photos/')

    def __str__(self):
        return self.name


# ------------------------
# ArtistConnect Model
# ------------------------
class ArtistConnect(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to='artists/', blank=True, null=True)

    def __str__(self):
        return self.name


# ------------------------
# ComedyPost Model
# ------------------------
class ComedyPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='comedy_images', blank=True, null=True)
    video = models.FileField(upload_to='comedy_videos', blank=True, null=True)
    audio = models.FileField(upload_to='comedy_audio', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ------------------------
# Music Model
# ------------------------
class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='studio_app/song/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"


# ------------------------
# Video Model
# ------------------------
class Video(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='studio_app/videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"


# ------------------------
# News Model
# ------------------------
class News(models.Model):
    FILE_TYPE_CHOICES = [
        ('image', 'Image'),
        ('pdf', 'PDF'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='news_files')
    type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ------------------------
# Product Model
# ------------------------
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name


# ------------------------
# RecordLabelDeal Model
# ------------------------
class RecordLabelDeal(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    document = models.FileField(upload_to='record_label_deals/', blank=True, null=True)

    def __str__(self):
        return self.title


# ------------------------
# SocialNews Model
# ------------------------
class SocialNews(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='social_news/', blank=True, null=True)

    def __str__(self):
        return self.title


# ------------------------
# TrendingItem Model
# ------------------------
class TrendingItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    audio_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


# ------------------------
# TrendingNews Model
# ------------------------
class TrendingNews(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    document = models.FileField(upload_to='trending_news_documents/', blank=True, null=True)

    def __str__(self):
        return self.title


# ------------------------
# Profile Model
# ------------------------
class Profile(models.Model):
    ROLE_CHOICES = [
        ('artist', 'Artist'),
        ('listener', 'Listener'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='listener')

    favorite_artists = models.ManyToManyField(Artist, related_name='favorited_by_profiles', blank=True)
    favorite_songs = models.ManyToManyField(Music, related_name='favorited_by_profiles', blank=True)
    favorite_videos = models.ManyToManyField(Video, related_name='favorited_by_profiles', blank=True)

    def __str__(self):
        return self.user.username


# ------------------------
# AuthorizationPin Model
# ------------------------
class AuthorizationPin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    authorization_pin = models.CharField(max_length=50, default='fadiya1234')
   
    def __str__(self):
        return f"Authorization Pin for {self.user.username}"



#class Music(models.Model):
#    title = models.CharField(max_length=255)
#    artist = models.CharField(max_length=255)
#    audio_file = models.FileField(upload_to='music/')
#    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#    upload_date = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return f"{self.title} - {self.artist}"



class MusicAuthorizationPin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    authorization_pin = models.CharField(max_length=50, default='fadiya1234')

    def __str__(self):
        return f"Music Authorization for {self.user.username if self.user else 'Guest'}"


# ------------------------
# Site configuration and slides (for dynamic logo & slideshow)
# ------------------------
class SiteConfiguration(models.Model):
    site_name = models.CharField(max_length=255, default='Tweet Music Records')
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Configuration'
        verbose_name_plural = 'Site Configuration'

    def __str__(self):
        return "Site Configuration"


class SlideImage(models.Model):
    SECTION_CHOICES = [
        ('hero', 'Hero'),
        ('secondary', 'Secondary'),
    ]

    section = models.CharField(max_length=50, choices=SECTION_CHOICES, default='hero')
    image = models.ImageField(upload_to='site/slides/')
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    caption = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.section} - {self.order}"
