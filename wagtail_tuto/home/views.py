# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from wagtail.core.models import Site

from home.models import CopyWritingSettings


def home(request):
    site = Site.find_for_request(request)
    social_media_setting = CopyWritingSettings.for_site(site)
    context = {'social_media_setting': social_media_setting}
    return render(request, 'home/home_page.html', context=context)
