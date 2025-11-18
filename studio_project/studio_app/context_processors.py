from .models import SiteConfiguration, SlideImage


def site_config(request):
    """Context processor to expose site-wide configuration and hero slides."""
    try:
        config = SiteConfiguration.objects.first()
    except Exception:
        config = None

    try:
        hero_slides = SlideImage.objects.filter(section='hero', active=True).order_by('order')
    except Exception:
        hero_slides = []

    return {
        'site_config': config,
        'hero_slides': hero_slides,
    }
