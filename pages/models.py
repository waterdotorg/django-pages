from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import get_script_prefix
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import iri_to_uri, python_2_unicode_compatible


@python_2_unicode_compatible
class Page(models.Model):
    TEMPLATE_CHOICES = getattr(settings, 'PAGE_TEMPLATES', (
        ('pages/default.html', 'Default'),
    ))

    url = models.CharField(_('URL'), max_length=100, db_index=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    template_name = models.CharField(
        _('template name'),
        max_length=100,
        choices=TEMPLATE_CHOICES,
        default=TEMPLATE_CHOICES[0][0],
    )
    registration_required = models.BooleanField(
        _('registration required'),
        default=False,
        help_text=_(
            "If this is checked, only logged-in users will be able to view "
            "the page."
        ),
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('url', '-created_date')

    def __str__(self):
        return "%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        # Handle script prefix manually because we bypass reverse()
        return iri_to_uri(get_script_prefix().rstrip('/') + self.url)
