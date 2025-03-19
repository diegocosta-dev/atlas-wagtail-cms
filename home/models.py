from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    author_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    hero_heading = models.TextField(blank=False, max_length=255)
    hero_summary = models.TextField(blank=False, max_length=500)
    hero_cta_label = models.CharField(max_length=50, blank=True)
    hero_cta_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hero_cta_url = models.URLField(blank=True)

    content_panels = [
        FieldPanel('author_image'),
        FieldPanel('hero_heading'),
        FieldPanel('hero_summary'),
        FieldPanel('hero_cta_label'),
        FieldPanel('hero_cta_page'),
        FieldPanel('hero_cta_url'),
    ]

    @property
    def hero_cta_link(self):
        if self.hero_cta_page:
            return self.hero_cta_page.url
        elif self.hero_cta_url:
            return self.hero_cta_url
        return None
    
    @property
    def hero_cta_text(self):
        if self.hero_cta_label:
            return self.hero_cta_label
        elif self.hero_cta_page:
            return self.hero_cta_page.title
        return 'Read More'