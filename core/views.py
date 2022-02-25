from django.conf import settings
from django.shortcuts import render, redirect
from django.templatetags.static import static
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def favicon(request):
    return redirect(static(settings.FAVICON_RELATIVE_PATH))

def handle404(request, exception=None):
    return render(request, 'core/404.html')