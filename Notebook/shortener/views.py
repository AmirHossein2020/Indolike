from django.http import JsonResponse, HttpResponseRedirect
from .models import ShortURL
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string

# This view handles URL shortening requests and redirects short URLs to their original destinations.
def shorten_url_api(request):
    original_url = request.GET.get("url")
    if not original_url:
        return JsonResponse({"error": "URL parameter required"}, status=400)

    obj, created = ShortURL.objects.get_or_create(original_url=original_url)
    short_url = request.build_absolute_uri(f"/s/{obj.short_code}/")
    return JsonResponse({"short_url": short_url})


# This view redirects a short URL to its original URL.
def redirect_short_url(request, short_code):
    obj = get_object_or_404(ShortURL, short_code=short_code)
    return HttpResponseRedirect(obj.original_url)
