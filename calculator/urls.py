from django.urls import path
from . import views

urlpatterns = [
    path('', views.imt_calculator, name='imt'),
]
