from wagtail.core.models import Site
from blog.models import BlogPage


def blog_page(request):
    """
    To avoid multiple Wagtail site query in request-response cycle, you can use
    wagtail.contrib.legacy.sitemiddleware.SiteMiddleware
    """
    wagtail_site = Site.find_for_request(request)
    context = {
        'blog_page': BlogPage.objects.in_site(wagtail_site).first()
    }
    return context
