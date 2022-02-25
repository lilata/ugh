from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, reverse

from . import models
# Create your views here.
@login_required
def index(request):
    return redirect(reverse('iloveme:page', kwargs={'username': request.user.username}))

def page(request, username):
    user = User.objects.filter(username=username).first()
    if user is None or user.is_anonymous:
        raise Http404
    page = models.Page.objects.filter(user=user).first()
    if page is None:
        page = models.Page.objects.create(user_id=user.pk)
    return render(request, 'iloveme/page.html', {'page': page})

def links(request):
    if request.user.is_authenticated is False:
        return redirect(reverse('iloveme:page'))
    return render(request, 'iloveme/links.html')