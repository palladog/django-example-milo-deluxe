from django.urls import path
from . import views

urlpatterns = [
    path('yoda', views.index, name="yoda")
]
