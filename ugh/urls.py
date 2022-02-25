"""ugh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

if settings.DEBUG:
    admin_urlpatterns = [
        path('admin/', admin.site.urls)
    ]
else:
    admin_urlpatterns = [
        path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
        path(settings.ADMIN_BASE_URL, admin.site.urls),
    ]
urlpatterns = admin_urlpatterns + [
    path('', include('core.urls', namespace='core')),
    path('me/', include('iloveme.urls', namespace='iloveme')),
    path('account/', include('account.urls', namespace='account')),
    path('utils/', include('utils.urls', namespace='utils')),
]
handler404 = 'core.views.handle404'
