from django.shortcuts import render
from .forms import GazouForm

def index(request):
    params = {
        'title': 'Hello',
        'temp_list':"",
        'form': GazouForm()
    }

    return render(request, 'gazou/home.html', params)