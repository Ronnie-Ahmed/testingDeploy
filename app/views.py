from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import TestModel,AddPHoto
from .forms import PhotoForm
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def index(request):
    names=TestModel.objects.all()
    photos=AddPHoto.objects.all()
    
    if request.method=='POST':
        form=PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
      form=PhotoForm()
       
    context={
        "names":names,
        "photos":photos,
        'form':form
        
    }
    return render(request,"app/index.html",context)
