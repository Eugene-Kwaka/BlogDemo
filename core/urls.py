from django.urls import path
from core.views import *

urlpatterns=[
    path('', home, name="home"),
    path('about/', about, name="about"),
]