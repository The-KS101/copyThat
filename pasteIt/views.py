from django.shortcuts import render, redirect
from .models import urlTable
from .forms import ContentPasted 
import datetime
from datetime import timezone

#renders the index view which showcases a form and runs some data processing before entry creation in db
def index(request):
    return render(request, 'index.html')

def urlReceive(request, urlName):
    form = ContentPasted()
    try:
        #working on this, might look complicated now
        data = urlTable.objects.get(url=urlName)
        if datetime.datetime.now().replace(tzinfo=timezone.utc) > data.deletion_time and data.visited==True:
            data.delete()
            return give_populated_form_with_url(request, urlName)

        else:
            form = ContentPasted(initial={'url': data.url, 'text': data.text})
            data.visited = True
            data.save()
            return give_form(request, form, data.deletion_time)


    except:
        return give_populated_form_with_url(request, urlName)


#This is the function to returns a functional form

def give_form(request, form, deltime):
    context = {
        'form': form,
        'time': deltime,
    }
    return render(request, 'displayPasted.html', context)

#This gives the functional form with the url popualated

def give_populated_form_with_url(request, urlName):
    form = ContentPasted(initial={'url': urlName})
    if request.method == "POST":
        form = ContentPasted(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            text = form.cleaned_data['text']
            deletion_time = datetime.datetime.now() + datetime.timedelta(minutes=int(form.cleaned_data['delTime']))
            urlTable.objects.create(url=url, text=text, deletion_time=deletion_time)
            context = {
                'url': url
            }
            return render(request, 'created.html', context)
    context = {
        'form': form,
    }
    return render(request, 'pasted.html', context)