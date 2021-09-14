from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Lugat
def index(request):
    soz = request.GET.get('q','')
    if soz and soz!='':
         natija =Lugat.objects.filter(english__contains=soz).all()[:3]

    else:
        natija = None
    return render(request,'index.html',{'q':soz,'natija':natija})

