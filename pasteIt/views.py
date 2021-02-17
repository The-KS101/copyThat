from django.shortcuts import render, redirect
from .models import urlTable
from .forms import ContentPasted 
import datetime
from datetime import timezone

def index(request):
    form = ContentPasted()
    if request.method == "POST":
        form = ContentPasted(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            text = form.cleaned_data['text']
            deletion_time = datetime.datetime.now() + datetime.timedelta(minutes=int(form.cleaned_data['delTime']))
            urlTable.objects.create(url=url, text=text, deletion_time=deletion_time, visited=False)
            return render(request, 'created.html')


    context = {
        'form': form,
    }
    return render(request, 'index.html', context)

def urlReceive(request, urlName):
    form = ContentPasted()
    try:
        #working on this, might look complicated now
        
        data = urlTable.objects.get(url=urlName)
        if datetime.datetime.now().replace(tzinfo=timezone.utc) > data.deletion_time.replace(tzinfo=timezone.utc):
            data.delete()
            give_form(request)
            

        else:
            form = ContentPasted(initial={"urll":urlName})


        
    except:
        give_populated_form_with_url(request, urlName)


        # context = {
        #     'form': form,
        # }
        # return render(request, 'pasted.html', context)

    
    # form = ContentPasted(initial={'url': urlName, 'text':data.text })
    context = {
        'form': form,
    }
    return render(request, 'pasted.html', context)

#This is the function to returns a functional form

def give_form(request):
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

#This gives the functional form with the url popualated

def give_populated_form_with_url(request, urlName):
    form = ContentPasted(initial={'url': urlName})
    form.url = urlName
    if request.method == "POST":
        form = ContentPasted(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            text = form.cleaned_data['text']
            deletion_time = datetime.datetime.now() + datetime.timedelta(minutes=int(form.cleaned_data['delTime']))
            urlTable.objects.create(url=url, text=text, deletion_time=deletion_time)
            return render(request, 'created.html')

