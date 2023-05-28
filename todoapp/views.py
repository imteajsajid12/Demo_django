from django.shortcuts import render
from django.http import HttpResponse
# add models
from .models import Data


# Create your views here.

def index(request):
    return HttpResponse('Welcome')


def index1(request):
    data = Data.objects.all().values()
    return render(request, 'todoapp/frontend/index.html',
                  {
                      'data': data
                  })

def index3(request,id):
    return render(request,'todoapp/frontend/edit.html',
                  {
                    #  'data':Data.objects.get(id )
                  }
                  )
    