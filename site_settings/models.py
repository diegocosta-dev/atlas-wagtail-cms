from django.db import models
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.admin.panels import FieldPanel

# Create your models here.
@register_setting
class BrandSettings(BaseGenericSetting):
  logo = models.ForeignKey(
    "wagtailimages.Image",
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name="+",
  )

  panels = [
    FieldPanel("logo"),
  ]

@register_setting
class FooterLinks(BaseGenericSetting):
  github = models.URLField(blank=True, null=True)
  linkedin = models.URLField(blank=True, null=True)
  facebook = models.URLField(blank=True, null=True)
  instagram = models.URLField(blank=True, null=True)

  panels = [
    FieldPanel("instagram"),
    FieldPanel("facebook"),
    FieldPanel("linkedin"),
    FieldPanel("github"),
  ]