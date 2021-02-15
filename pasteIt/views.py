from django.shortcuts import render
from .forms import ContentPasted

def index(request):
    form = ContentPasted()
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)



def test(request):
 
    context = {
        
    }
    return render(request, 'test.html', context)