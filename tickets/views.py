from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Ticket
from .forms import TicketForm


class CreateTicketView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/create_ticket.html'
    success_url = reverse_lazy('inbox')

    def get_success_url(self):
        return self.success_url


class TicketListView(ListView):
    model = Ticket
    template_name = 'tickets/tickets.html'
    context_object_name = 'tickets'
