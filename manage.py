#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wagtail_tuto.settings.dev")

    from django.core.management import execute_from_command_line

    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_path, "wagtail_tuto"))

    execute_from_command_line(sys.argv)
