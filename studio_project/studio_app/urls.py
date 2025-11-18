from django.urls import path
from studio_app import views

app_name = 'studio_app'

urlpatterns = [
    path('index/', views.MusicUploadView.as_view(), name='index'),
    path('upload/music/', views.MusicUploadView.as_view(), name='upload_music'),
    path('music_authorization/', views.music_authorization, name='music_authorization'),
    #path('music/authorize/', views.music_authorization, name='music_authorization'),
    #path('music/upload/', views.upload_music, name='upload_music'),
    path('upload/video/', views.VideoUploadView.as_view(), name='upload_video'),
    
        
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('video_authorization/', views.video_authorization, name='video_authorization'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('artists/', views.artists, name='artists'),
    path('join/', views.join, name='join'),
    path('session/', views.session, name='session'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('whatsapp/', views.whatsapp, name='whatsapp'),
    path('faq/', views.faq, name='faq'),
    path('trending/', views.trending, name='trending'),
    path('record-label-deals/', views.record_label_deals, name='record_label_deals'),
    path('online-market-store/', views.online_market_store, name='online_market_store'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('social/', views.social, name='social'),
    path('artist_connect/', views.artist_connect, name='artist_connect'),
    path('artist/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('download-songs/', views.download_songs, name='download_songs'),
    path('download-videos/', views.download_videos, name='download_videos'),
    path('terms-conditions/', views.terms_conditions, name='terms_conditions'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('comedy-entertainment/', views.comedy_entertainment, name='comedy_entertainment'),
    path('create-comedy-post/', views.create_comedy_post, name='create_comedy_post'),
    path('advertise-products/', views.advertise_products, name='advertise_products'),
    path('products/<int:product_id>/delete/', views.product_delete, name='product_delete'),
    path('top-buttons/', views.top_buttons, name='top_buttons'),
]