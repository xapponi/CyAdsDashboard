from django.urls import path
from django.conf.urls import url
from catalog import views

from .views import index, chart, viewsbydate

urlpatterns = [
    path('', views.index, name='index'),
    path('chart', views.chart, name='chart'),
    path('viewsbydate', views.viewsbydate, name='bydate'),
]
