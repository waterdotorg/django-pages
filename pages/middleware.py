from django.conf import settings
from django.http import Http404

from pages.views import page


class PageFallbackMiddleware(object):
    def process_response(self, request, response):
        # No need to check for a page on non-404 responses.
        if response.status_code != 404:
            return response

        try:
            return page(request, request.path_info)
        # Return the original response if any errors happened. Because this
        # is a middleware, we can't assume the errors will be caught elsewhere.
        except Http404:
            return response
        except:
            if settings.DEBUG:
                raise
            return response
