from django.urls import path, include
from . import views

app_name = 'account'
api_urlpatterns = [
    path('user_exists/', views.api_user_exists, name='user_exists')
]
urlpatterns = [
    path('register/', views.registration, name='registration'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('api/', include(api_urlpatterns)),
]
