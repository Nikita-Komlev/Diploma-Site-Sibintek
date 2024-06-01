# tickets/urls.py
from django.contrib import admin
from django.urls import path
from .views import TicketListView, CreateTicketView, TicketDetailView, TicketUpdateView, TicketDeleteView, \
    TakeTicketView

urlpatterns = [
    path('', TicketListView.as_view(), name='inbox'),
    path('create/', CreateTicketView.as_view(), name='create_ticket'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('ticket/<int:pk>/edit/', TicketUpdateView.as_view(), name='ticket_update'),
    path('ticket/<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
    path('ticket/<int:pk>/take/', TakeTicketView.as_view(), name='take_ticket'),
]
