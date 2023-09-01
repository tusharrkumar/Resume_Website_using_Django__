from django.shortcuts import render

## Create your views here.


def home(request):
    d = {'home':'active'}
    return render(request, 'home.html', d)