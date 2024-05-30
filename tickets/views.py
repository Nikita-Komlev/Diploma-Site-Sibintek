# tickets/views.py
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Ticket
from .forms import TicketForm


class CreateTicketView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/create_ticket.html'
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.success_url


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'tickets/tickets.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Ticket.objects.all()  # Для сотрудников
        else:
            return Ticket.objects.filter(user=user)  # Для обычных пользователей

class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'tickets/ticket_detail.html'
    context_object_name = 'ticket'

class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_form.html'

    def get_success_url(self):
        return reverse('ticket_detail', kwargs={'pk': self.object.pk})


class TicketDeleteView(LoginRequiredMixin, DeleteView):
    model = Ticket
    template_name = 'tickets/ticket_confirm_delete.html'
    success_url = reverse_lazy('inbox')