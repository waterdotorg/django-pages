from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from pages.forms import PageForm
from pages.models import Page


class PageAdmin(admin.ModelAdmin):
    form = PageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content')}),
        (_('Advanced'), {
            'classes': ('collapse',),
            'fields': ('registration_required', 'template_name')
        }),
    )
    list_display = ('url', 'title')
    list_filter = ('registration_required',)
    search_fields = ('url', 'title')

admin.site.register(Page, PageAdmin)
