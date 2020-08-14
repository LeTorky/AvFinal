from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
def av(request):
    x = avdate.objects.get(id=1)
    if request.method == 'GET':
        av1=0
        form = Passcode(request.GET)
        context = {
            'form': form,
            'av1': av1,
        }
        return render(request,'av.html', context)
    elif request.method == 'POST':
        av1 = 0
        form = Passcode(request.POST)
        if form.is_valid():
            x = avdate.objects.get(id=1)
            x.num = x.num+1
            x.save()
            p = form.cleaned_data['name']
            if p == 'circularbed':
                av1 = 1
        context = {
            'form': form,
            'av1': av1,
            'date': x,
        }

        return render(request, 'av.html', context)
