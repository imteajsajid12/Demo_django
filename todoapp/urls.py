from django.urls import path
from . import views


urlpatterns= [
    path("sajid/",views.index),
    path("imteajsajid/",views.index1),
    path('imteaj/edit/<id>',views.index3 ,name='edit')
]