from django.urls import path
from . import views

#flight routes

urlpatterns =[
    path('',views.index)
]