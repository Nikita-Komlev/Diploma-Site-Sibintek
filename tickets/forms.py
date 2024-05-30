# tickets/forms.py
from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('subject', 'description', 'urgent')
        labels = {
            'subject': 'Тема заявки',
            'description': 'Описание заявки',
            'urgent': 'Срочность'
        }
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'appearance-none border rounded-lg bg-zinc-300 w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'cols': 40,
                'class': 'appearance-none border rounded-lg bg-zinc-300 w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'
            }),
            'urgent': forms.Select(attrs={
                'class': 'appearance-none border rounded-lg bg-zinc-300 w-full py-2 px-3 leading-tight focus:outline-none focus:shadow-outline '}),

        }
