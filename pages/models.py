import os

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings



class Page(models.Model):
    title = models.CharField(max_length=200, blank=True, verbose_name=_("Title"))
    extend_title = models.BooleanField(default=True, verbose_name=_("Extend default title"))
    section = models.ForeignKey('self', blank=True, null=True, limit_choices_to = {'section': None, 'title__gt': ''}, verbose_name=_("Section"))
    url = models.CharField(max_length=200, blank=True, verbose_name=_("URL"))
    old_url = models.CharField(max_length=200, blank=True, verbose_name=_("Old URL"))
    text = models.TextField(blank=True, verbose_name=_("HTML text"))
    active = models.BooleanField(default=True, verbose_name=_("Active page"))
    
    def __unicode__(self):
        return self.title


class PageFile(models.Model):
    page = models.ForeignKey('Page', verbose_name=_("Page"))
    file = models.FileField(upload_to=settings.MEDIA_ROOT, blank=True, null=True, verbose_name=_("File"))
    #file = models.FileField(upload_to=os.path.join(settings.MEDIA_ROOT, page.url), blank=True, null=True, verbose_name=_("File"))
