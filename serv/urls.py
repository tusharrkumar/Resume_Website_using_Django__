from django.urls import path
from serv.views import *
# app_name = 'service'

urlpatterns = [
    path('service/',service,name='service'),
]