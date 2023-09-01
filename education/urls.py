from django.urls import path
from education.views import *
# app_name = 'education'

urlpatterns = [
    path('skill/',skill,name='skill'),
]