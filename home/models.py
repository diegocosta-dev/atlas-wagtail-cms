from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class HomePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    heading = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=False, max_length=500)
    cta_label = models.CharField(max_length=50, blank=True)
    cta_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    cta_url = models.URLField(blank=True)

    my_story_heading = models.CharField(max_length=255, blank=True, default="My Story")
    my_story_content = models.TextField(blank=True, max_length=800)

    content_panels = [
        FieldPanel('image'),
        FieldPanel('heading'),
        FieldPanel('summary'),
        MultiFieldPanel([
            FieldPanel('cta_label'),
            FieldPanel('cta_page'),
            FieldPanel('cta_url'),
        ], heading="CTA Buttom"),
        MultiFieldPanel([
            FieldPanel('my_story_heading'),
            FieldPanel('my_story_content'),
        ], heading="My Story")
    ]

    @property
    def cta_link(self):
        if self.cta_page:
            return self.cta_page.url
        elif self.cta_url:
            return self.cta_url
        return None
    
    @property
    def cta_text(self):
        if self.cta_label:
            return self.cta_label
        elif self.cta_page:
            return self.cta_page.title
        return 'Read More'
    
    def get_context(self, request):
        context = super().get_context(request)
        context['blog_posts'] = ['1', '2', '3']
        # context['blog_posts'] = BlogPage.objects.live().public().orderBy('-first_published_at')[:3]
        return context