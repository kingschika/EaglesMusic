from django.shortcuts import render, redirect
from django.views.generic import View
from studio_app.forms import MusicForm, VideoForm,ProfileForm, UserRegistrationForm, VideoAuthorizationForm,  MusicAuthorizationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import  Music, Video, Artist, Profile
from datetime import datetime
from django.shortcuts import render, redirect
from .models import News
from django.core.mail import send_mail
from .models import TrendingItem, TrendingNews
from .models import RecordLabelDeal
from django.shortcuts import render, get_object_or_404
from .models import Product,SocialNews, ArtistConnect
from .models import ComedyPost
from .forms import ComedyPostForm
from django.contrib.auth.models import User
from .forms import MusicAuthorizationForm




# Create your views here.


class MusicUploadView(View):
    
    def get(self, request):
        form = MusicForm()
        return render(request, 'studio_app/upload_music.html', {'form': form, 'now': datetime.now()})

    def post(self, request):
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('studio_app:index')
        return render(request, 'studio_app/upload_music.html', {'form': form, 'now': datetime.now()})


def music_authorization(request):
    if request.method == 'POST':
        form = MusicAuthorizationForm(request.POST)
        if form.is_valid():
            return redirect('studio_app:upload_music')  # Redirect to your upload music page
        else:
            from django.contrib import messages
            messages.error(request, "Invalid or mismatched authorization pin.")
    else:
        form = MusicAuthorizationForm()
    return render(request, 'studio_app/music_authorization.html', {'form': form, 'now': datetime.now()})



'''
def music_authorization(request):
    if request.method == 'POST':
        form = MusicAuthorizationForm(request.POST)
        if form.is_valid():
            entered_pin = form.cleaned_data['authorization']
            if entered_pin == form.authorization_pin:
                messages.success(request, 'Authorization successful. You can now upload music.')
                return redirect('studio_app:upload_music')
            else:
                messages.error(request, 'Invalid authorization pin. Please try again.')
    else:
        form = MusicAuthorizationForm()
    return render(request, 'studio_app/music_authorization.html', {'form': form})

@login_required
def upload_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save(commit=False)
            music.uploaded_by = request.user
            music.save()
            messages.success(request, 'Your music was uploaded successfully!')
            return redirect('studio_app:home')
        else:
            messages.error(request, 'There was an error uploading your music. Please try again.')
    else:
        form = MusicForm()
    return render(request, 'studio_app/upload_music.html', {'form': form})

'''


class VideoUploadView(View):
    def get(self, request):
        form = VideoForm()
        return render(request, 'studio_app/upload_video.html', {'form': form, 'now': datetime.now()})
 
    def post(self, request):
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('studio_app:index')
        return render(request, 'studio_app/upload_video.html', {'form': form, 'now': datetime.now()})
    

def home(request):
    songs = Music.objects.all()
    music = Music.objects.all()
    videos = Video.objects.all()
    return render(request, "studio_app/home.html", {'songs': songs, 'music': music, 'videos': videos, 'now': datetime.now()})


@login_required
def dashboard(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    # Get favorites
    favorite_songs = profile.favorite_songs.all()
    favorite_artists = profile.favorite_artists.all()
    favorite_videos = profile.favorite_videos.all()

    # Check if profile is complete
    is_profile_complete = bool(profile.bio and profile.profile_picture)

    context = {
        'user': request.user,
        'profile': profile,
        'favorite_songs': favorite_songs,
        'favorite_artists': favorite_artists,
        'favorite_videos': favorite_videos,
        'is_profile_complete': is_profile_complete,
        'now': datetime.now(),
    }

    return render(request, 'studio_app/dashboard.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            #Profile.objects.create(user=user)
            return redirect('studio_app:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'studio_app/register.html', {'form': form, 'now': datetime.now()})
  
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('studio_app:dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'studio_app/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('studio_app:login')



@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'studio_app/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('studio_app:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'studio_app/edit_profile.html', {'form': form})



def video_authorization(request):
    if request.method == 'POST':
        form = VideoAuthorizationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Authorization successful! You may now upload your video.")
            return redirect('studio_app:upload_video')
        else:
            messages.error(request, "Invalid authorization pin. Please try again.")
    else:
        form = VideoAuthorizationForm()
    return render(request, 'studio_app/video_authorization.html', {'form': form, 'now': datetime.now()})



def contact(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(f"Message from {name}", message, email, ['your_email@example.com'])
        return redirect('studio_app:home')
    return render(request, 'studio_app/contact.html',{'now': datetime.now()})



def news(request):
    news_items = [
        {
            'title': 'New Music Release',
            'description': 'Check out our latest music release from our top artists.',
            'published_at': datetime(2025, 9, 1),
            'type': 'image',
            'file': {'url': 'https://example.com/image.jpg'},
        },
        {
            'title': 'Upcoming Concert',
            'description': 'Join us for an exciting concert featuring some of the biggest names in music.',
            'published_at': datetime(2024, 10, 15),
            'type': 'pdf',
            'file': {'url': 'https://example.com/concert.pdf'},
        },
        {
            'title': 'Artist Spotlight',
            'description': 'Get to know our featured artist of the month and learn more about their music.',
            'published_at': datetime(2024, 9, 15),
            'type': 'image',
            'file': {'url': 'https://example.com/artist.jpg'},
        },
    ]
    return render(request, 'studio_app/news.html', {'news_items': news_items, 'now': datetime.now()})




def about(request):
    about_info = {
        'story': 'Tweet Music Records was founded in 2010 with a passion for discovering and nurturing new talent. Over the years, we have grown to become one of the leading record labels in the industry, working with some of the biggest names in music.',
        'mission': 'Our mission is to provide a platform for artists to showcase their talent and connect with their fans. We believe in fostering creativity and innovation, and we strive to push the boundaries of what is possible in the music industry.',
        'team': 'Our team is made up of experienced professionals who are dedicated to supporting our artists and helping them achieve their goals. From A&R to marketing and promotion, we have a team of experts who are passionate about music and committed to delivering high-quality results.',
    }
    return render(request, 'studio_app/about.html', {'about': about_info, 'now': datetime.now()})



def artists(request):
    artists_info = [
        {
            'name': 'John Doe',
            'bio': 'John Doe is a talented singer-songwriter known for his soulful voice and catchy melodies.',
            'image': 'https://example.com/johndoe.jpg',
        },
        {
            'name': 'Jane Smith',
            'bio': 'Jane Smith is a rising star in the music industry, known for her powerful vocals and energetic live performances.',
            'image': 'https://example.com/janesmith.jpg',
        },
        {
            'name': 'Bob Johnson',
            'bio': 'Bob Johnson is a seasoned musician with a passion for rock music. He has been performing for over a decade and has a loyal fan base.',
            'image': 'https://example.com/bobjohnson.jpg',
        },
    ]
    return render(request, 'studio_app/artists.html', {'artists': artists_info, 'now': datetime.now()})


def join(request):
    if request.method == 'POST':
        name = request.POST['name']
        whatsapp = request.POST['whatsapp']
        email = request.POST['email']
        bio = request.POST['bio']
        demo = request.FILES['demo']

        # Send email to record label
        send_mail(
            'New Artist Submission',
            f'Name: {name}\nWhatsapp: {whatsapp}\nEmail: {email}\nBio: {bio}',
            email,
            ['recordlabel@example.com'],
            fail_silently=False,
        )

        return redirect('studio_app:home')
    return render(request, 'studio_app/join.html', {'now': datetime.now()})





def session(request):
    if request.method == 'POST':
        name = request.POST['name']
        whatsapp = request.POST['whatsapp']
        email = request.POST['email']
        session = request.POST['session']
        demo = request.FILES['demo']

        # Send email to record label
        send_mail(
            'New Artist Submission',
            f'Name: {name}\nWhatsapp: {whatsapp}\nEmail: {email}\nSession: {session}',
            email,
            ['recordlabel@example.com'],
            fail_silently=False,
        )

        return redirect('studio_app:home')
    return render(request, 'studio_app/session.html', {'now': datetime.now()})


def whatsapp(request):
    return render(request, 'studio_app/whatsapp.html', {'now': datetime.now()})



def faq(request):
    return render(request, 'studio_app/faq.html', {'now': datetime.now()})


def trending(request):
    trending_items = TrendingItem.objects.all()
    trending_news = TrendingNews.objects.all()
    return render(request, 'studio_app/trending.html', {'trending_items': trending_items, 'trending_news': trending_news, 'now': datetime.now()})


def record_label_deals(request):
    record_label_deals = RecordLabelDeal.objects.all()
    return render(request, 'studio_app/record_label_deals.html', {'record_label_deals': record_label_deals, 'now': datetime.now()})



def online_market_store(request):
    products = Product.objects.all()
    return render(request, 'studio_app/online_market_store.html', {'products': products, 'now': datetime.now()})


def product_list(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'studio_app/product_list.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'studio_app/product_detail.html', {'product': product, 'now':datetime.now()})


def social(request):
    social_news = SocialNews.objects.all()
    return render(request, 'studio_app/social.html', {'social_news': social_news, 'now': datetime.now()}) 
 

def artist_connect(request):
    artist = ArtistConnect.objects.all()
    return render(request, 'studio_app/artist_connect.html', {'artist': artist, 'now': datetime.now()})

def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'studio_app/artist_detail.html', {'artist': artist})

def download_songs(request):
    songs = Music.objects.all()
    return render(request, 'studio_app/download_songs.html', {'songs': songs})


def download_videos(request):
    videos = Video.objects.all()
    return render(request, 'studio_app/download_video.html', {'videos': videos})


def terms_conditions(request):
    return render(request, 'studio_app/terms_conditions.html')

def privacy_policy(request):
    return render(request, 'studio_app/privacy_policy.html')



def comedy_entertainment(request):
    posts = ComedyPost.objects.all().order_by('-created_at')
    return render(request, 'studio_app/comedy_entertainment.html', {'posts': posts})

def create_comedy_post(request):
    if request.method == 'POST':
        form = ComedyPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('studio_app:comedy_entertainment')
    else:
        form = ComedyPostForm()
    return render(request, 'studio_app/create_comedy_post.html', {'form': form})


def advertise_products(request):
    return render(request, 'studio_app/advertise_products.html', {'now': datetime.now()})


def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully')
        return redirect('product_list')
    return render(request, 'studio_app/product_confirm_delete.html', {'product': product})

def top_buttons(request):
    return render(request, 'studio_app/top_buttons.html')