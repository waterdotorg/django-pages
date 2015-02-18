from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from pages.forms import PageForm
from pages.models import Page


class PageAdmin(admin.ModelAdmin):
    form = PageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content')}),
        (_('Advanced'), {
            'fields': ('registration_required', 'published', 'template_name')
        }),
    )
    list_display = ('url', 'title', 'published', 'created_date')
    list_filter = ('registration_required', 'published')
    search_fields = ('url', 'title')

admin.site.register(Page, PageAdmin)
