from django.urls import path
from django.conf.urls import url
from catalog import views

from .views import index

urlpatterns = [
    path('', views.index, name='index'),
]
