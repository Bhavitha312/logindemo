from django.urls import path
from demo import views

urlpatterns = [

    path('display', views.display, name='display')
   
]
