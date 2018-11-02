from django.shortcuts import render

# Create your views here.
from catalog.models import *
def index(request):

    context = {
        'hello': 'Hello World!',
    }

    return render(request, 'index.html', context=context)
