from django.urls import path, include
from . import views
app_name = 'utils'
api_urlpatterns = [
    path('new_captcha/', views.new_captcha, name='new_captcha'),
    path('delete_captcha/', views.delete_captcha, name='delete_captcha'),
]
urlpatterns = [
    path('api/', include(api_urlpatterns))
]