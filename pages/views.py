from django.conf import settings
from django.core.cache import cache 
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.template import loader, RequestContext
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect

from pages.models import Page


def page(request, url):
    if not url.startswith('/'):
        url = '/' + url

    if not url.endswith('/') and settings.APPEND_SLASH:
        return HttpResponsePermanentRedirect('%s/' % request.path)

    page_cache = cache.get(url)

    if page_cache:
        return page_cache

    try:
        obj = get_object_or_404(Page, url__iexact=url, published=True)
    except Http404:
        raise

    rp = render_page(request, obj)

    page_cache_timeout = getattr(settings, 'PAGE_CACHE_TIMEOUT', 300)

    cache.set(url, rp, page_cache_timeout)

    return rp


@csrf_protect
def render_page(request, obj):
    # If registration is required for accessing this page, and the user isn't
    # logged in, redirect to the login page.
    if obj.registration_required and not request.user.is_authenticated():
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.path)

    # If the template is unavailable an exception will be raised.
    # Update the database prior to removing a template.
    t = loader.get_template(obj.template_name)

    # To avoid having to always use the "|safe" filter in page templates,
    # mark the title and content as safe since they are raw HTML
    obj.title = mark_safe(obj.title)
    obj.content = mark_safe(obj.content)

    c = RequestContext(request, {
        'page': obj,
    })
    response = HttpResponse(t.render(c))
    return response
