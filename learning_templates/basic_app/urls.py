from django.urls import path
from .views import *

#template ttagging
app_name= 'basic_app'

urlpatterns=[

    path('relative/',relative,name='relative'),
    path('other/',other,name='other'),
    

]