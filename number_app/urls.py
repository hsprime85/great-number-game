from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('guess_number', views.guess_number),
    path('reset', views.reset),
]
