from django.urls import path
from . import views


urlpatterns= [
    path("sajid/",views.index),
    path("imteajsajid/",views.index1,name="imteajsajid"),
    path("imteajsajid/save",views.Add_data, name='savedata'),
    path('imteajsajid/update/<id>',views.update_data, name='update_data'),
    path('imteaj/edit/<id>',views.index3 ,name='edit'),
    path('imteaj/delete/<id>',views.delete ,name='delete')
]