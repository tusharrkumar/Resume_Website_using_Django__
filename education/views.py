from django.shortcuts import render

## Create your views here.

def skill(request):
    d = {'skill':'active'}
    return render(request, 'skills.html',d)
