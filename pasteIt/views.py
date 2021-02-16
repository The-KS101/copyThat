from django.shortcuts import render, redirect
from .models import urlTable
from .forms import ContentPasted 
import datetime

def index(request):
    form = ContentPasted()
    if request.method == "POST":
        form = ContentPasted(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            text = form.cleaned_data['text']
            deletion_time = datetime.datetime.now() + datetime.timedelta(minutes=int(form.cleaned_data['delTime']))
            urlTable.objects.create(url=url, text=text, deletion_time=deletion_time)
            return render(request, 'created.html')


    context = {
        'form': form,
    }
    return render(request, 'index.html', context)

def urlReceive(request, urlName):
    form = ContentPasted()
    try:
        data = urlTable.objects.get(url=urlName)
    except:
        form = ContentPasted()
        form.url = urlName
        if request.method == "POST":
            form = ContentPasted(request.POST)
            if form.is_valid():
                url = form.cleaned_data['url']
                text = form.cleaned_data['text']
                deletion_time = datetime.datetime.now() + datetime.timedelta(minutes=int(form.cleaned_data['delTime']))
                urlTable.objects.create(url=url, text=text, deletion_time=deletion_time)
                return render(request, 'created.html')


        context = {
            'form': form,
        }
        return render(request, 'pasted.html', context)
    
    form = ContentPasted()
    context = {
        'form': form,
    }
    return render(request, 'pasted.html', context)