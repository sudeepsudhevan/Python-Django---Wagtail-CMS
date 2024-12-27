from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    banner_title = models.CharField(max_length=100, default='Welcome to my homepage!')

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
    ]