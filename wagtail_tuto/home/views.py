# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from home.models import CopyWritingSettings

from wagtail.core.models import Site

def home(request):
    social_media_setting = CopyWritingSettings.for_site(Site.find_for_request(request))
    context = {'social_media_setting': social_media_setting}
    return render(request, 'home/home_page.html', context=context)
