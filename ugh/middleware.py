from uuid import uuid4
from ipware import get_client_ip
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
class AdminDirectLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if settings.DEBUG:
            return response
        url = settings.ADMIN_DIRECT_LOGIN_URL
        url_stripped = url.rstrip('/')
        if request.path == url or request.path == url_stripped:
            client_ip, _ = get_client_ip(request)
            if client_ip and client_ip in settings.ADMIN_DIRECT_LOGIN_IPS:
                admin_user = User.objects.filter(
                    is_superuser=True,
                    is_staff=True,
                ).first()
                if admin_user is None:
                    if settings.ADMIN_DIRECT_LOGIN_CREATE_USER_IF_NOT_EXIST is False:
                        return response
                    admin_user = User.objects.create_user(
                        str(uuid4()),
                        is_staff=True,
                        is_superuser=True,
                    )
                login(request, admin_user)
                return redirect('/' + settings.ADMIN_BASE_URL)
        return response
