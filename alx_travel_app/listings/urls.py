# listings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from django.urls import path
from .views import sample_api

urlpatterns = [
    path('sample/', sample_api),
]
