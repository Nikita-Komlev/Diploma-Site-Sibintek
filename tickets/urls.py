from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TicketListView.as_view(), name='inbox'),
    path('create/', views.CreateTicketView.as_view(), name='create_ticket'),

]
