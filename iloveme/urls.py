from django.urls import path

from . import views
app_name = 'iloveme'
urlpatterns = [
    path('', views.index, name='index'),
    path('links/', views.links, name='links'),
    path('<str:username>/', views.page, name='page'),
]