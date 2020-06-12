from django.urls import path
from . import views

#flight routes

urlpatterns =[
    path('',views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/boook", views.book, name="book")
]