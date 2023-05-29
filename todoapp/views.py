from django.shortcuts import render
from django.http import HttpResponse
# add models
from .models import Data
from django.shortcuts import redirect, reverse
from django.contrib import messages
# Create your views here.


def index(request):
    return HttpResponse('Welcome')


def index1(request):
    
    data = Data.objects.all().values()
    return render(request, 'todoapp/frontend/index.html',
                  {
                      'data': data
                  })

    # insurt data


def Add_data(request):
    data = Data()
    data.title = request.POST.get('title')
    data.slug = request.POST.get('slug')
    data.descriptions = request.POST.get('descriptions')
    data.save()
    messages.success(request, "Data Save  Successfully.")
    return redirect(reverse('imteajsajid'))


def index3(request, id):
    data = Data.objects.all().values()
    edit_data = Data.objects.get(id=id)
    # return HttpResponse(id)
    return render(request, 'todoapp/frontend/edit.html',
                  {
                      'data': data,
                      'edit_data': edit_data
                  }
                  )


def update_data(request, id):
    data = Data.objects.get(id=id)
    # return HttpResponse(data)
    data.title = request.POST.get('title')
    data.slug = request.POST.get('slug')
    data.descriptions = request.POST.get('descriptions')
    data.save()
    messages.success(request, "Data Update Successfully.")
    return redirect(reverse('imteajsajid'))


def delete(request, id):
    data = Data.objects.get(id=id)
    data.delete()
    messages.error(request, "Document deleted.")
    return redirect(reverse('imteajsajid'))
