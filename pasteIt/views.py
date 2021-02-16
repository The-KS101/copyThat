from django.shortcuts import render
from .forms import ContentPasted, DispPasted

def index(request):
    form = ContentPasted()
    if request.method == "POST":
        form = ContentPasted(request.POST)

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)

def urlReceive(request, urlname):
    form = DispPasted()
    if request.method == "GET":
        form = dispPasted(request.GET)
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)