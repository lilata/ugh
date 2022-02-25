import json

from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from utils.models import Captcha
from utils.utils import updated_dict

from . import utils

# Create your views here.

def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('core:index'))
    if request.method == 'GET':
        return render(request, 'account/registration.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_again = request.POST.get('password_again')
        captcha = request.POST.get('captcha')
        captcha_token = request.POST.get('captcha_token')
        template_data = {'username': username}
        on_bad_data = lambda d=None: \
            render(request, 'account/registration.html', updated_dict(template_data, d))
        if not captcha or not captcha_token or not username:
            return on_bad_data()
        c = Captcha.objects.filter(token=captcha_token).first()
        if c is None:
            return on_bad_data()
        if c.check_answer_and_delete(captcha) is False:
            return on_bad_data({'msg': 'Incorrect captcha answer! '
                                       'Please note that the answer is case-sensitive.'})
        if password != password_again:
            return on_bad_data()
        if utils.check_password(password) is False:
            return on_bad_data()
        user_exists = User.objects.filter(username=username).first() is not None
        if user_exists:
            return on_bad_data()
        User.objects.create_user(username=username, password=password)
        return render(request, 'account/after_registration.html', {
            'username': username,
        })


def login_user(request):
    if request.user.is_authenticated:
        next_url = request.GET.get('next') or request.POST.get('next')
        if isinstance(next_url, str) and next_url.startswith('/'):
            return redirect(next_url)
        return redirect(reverse('core:index'))
    if request.method == 'GET':
        return render(request, 'account/login.html')
    if request.method == 'POST':
        data = request.POST
        on_bad_request = lambda d=None: render(request, 'account/login.html',
                                        updated_dict({'msg': 'Bad request!',
                                                      'next': data.get('next')}, d))
        if data is None:
            return on_bad_request()
        username = data.get('username')
        password = data.get('password')
        captcha = data.get('captcha')
        captcha_token = data.get('captcha_token')
        if not username or not password or not captcha or not captcha_token:
            return on_bad_request()
        c = Captcha.objects.filter(token=captcha_token).first()
        if c is None:
            return on_bad_request({'msg': 'Captcha has expired'})
        if c.check_answer_and_delete(captcha) is False:
            return on_bad_request({'msg': 'Invalid Captcha answer!'
                                          'Please note that the answer is case-sensitive.'})
        user = authenticate(username=username, password=password)
        if user is None:
            return on_bad_request({'msg': 'Invalid username or password =3'})
        login(request, user)
        next_url = data.get('next', '')
        if next_url.startswith('/'):
            return redirect(next_url)
        return redirect(reverse('core:index'))

@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse('core:index'))

@login_required
def dashboard(request):
    pass

@api_view(['POST'])
def api_user_exists(request):
    try:
        data = json.loads(str(request.body, encoding='utf-8'))
        username = data.get('username')
    except json.JSONDecodeError:
        return Response(status=400)
    if not username:
        return Response(status=400)
    u = User.objects.filter(username=username).first()
    return Response({"message": u is not None})