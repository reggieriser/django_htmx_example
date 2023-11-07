from django.shortcuts import render

from .models import DutyLocation


def search(request):
    search_term = request.GET.get("search", "")
    has_more = False
    if search_term:
        duty_locations = DutyLocation.objects.filter(name__icontains=search_term).order_by("name")[:51]
        if len(duty_locations) > 50:
            has_more = True
    else:
        duty_locations = None
    if request.htmx:
        template_to_render = "locations/partials/results.html"
    else:
        template_to_render = "locations/location_search.html"
    return render(request, template_to_render, {"duty_locations": duty_locations, "has_more": has_more})
