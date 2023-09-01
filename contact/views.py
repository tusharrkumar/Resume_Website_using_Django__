from django.shortcuts import render

## Create your views here.

def contact_page(request):
    d = {'contact':'active'}
    return render(request, 'contact.html', d)
