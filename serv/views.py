from django.shortcuts import render

## Create your views here.


def service(request):
    d = {'service':'active'}
    return render(request, 'service.html',d)