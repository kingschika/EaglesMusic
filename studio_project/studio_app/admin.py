from django.contrib import admin
from studio_app.models import Music, Video, Artist, Profile
from .models import TrendingItem, TrendingNews
from .models import RecordLabelDeal,Product, SocialNews, ArtistConnect
from .models import MusicAuthorizationPin
from .models import SiteConfiguration, SlideImage
from django.utils.html import format_html

@admin.register(MusicAuthorizationPin)
class MusicAuthorizationPinAdmin(admin.ModelAdmin):
    list_display = ('user', 'authorization_pin')


admin.site.register(Music)
admin.site.register(Video)
admin.site.register(Artist)
admin.site.register(TrendingItem)
admin.site.register(TrendingNews)
admin.site.register(RecordLabelDeal)
admin.site.register(Product)
admin.site.register(SocialNews)
admin.site.register(ArtistConnect)
admin.site.register(SlideImage)


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'logo_preview', 'updated_at')
    readonly_fields = ('logo_preview',)

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height:80px;"/>', obj.logo.url)
        return "-"

    logo_preview.short_description = 'Logo Preview'



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'bio')
    search_fields = ('user__username', 'role')
