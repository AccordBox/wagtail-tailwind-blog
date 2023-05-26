from wagtail.core.models import Site
from wagtail_app.site.models import SitePage


def site_page(request):
    wagtail_site = Site.find_for_request(request)
    context = {
        'site_page': SitePage.objects.in_site(wagtail_site).first()
    }
    return context
