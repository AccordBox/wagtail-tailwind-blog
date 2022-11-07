"""wagtail_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views import defaults as default_views

from wagtail.core import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap
import wagtail_app.blog.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('sitemap.xml', sitemap),
    path('robots.txt', wagtail_app.blog.views.RobotsView.as_view()),
    path('comments/', include('wagtail_app.custom_comments.urls')),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    path('', include(wagtail_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        path('404/', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
        path('500/', default_views.server_error),
    ] + urlpatterns
