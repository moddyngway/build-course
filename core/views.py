from django.shortcuts import render
from django.template import RequestContext


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)