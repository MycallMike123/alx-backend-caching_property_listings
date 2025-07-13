from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property

# Create your views here.

@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    properties = get_all_properties()
    return JsonResponse({'data': properties})
