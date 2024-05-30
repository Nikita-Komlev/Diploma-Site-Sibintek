# tickets/models.py
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Ticket(models.Model):
    URGENCY_CHOICES = [
        ('Low', 'Низкая'),
        ('Medium', 'Средняя'),
        ('High', 'Высокая'),
    ]

    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In process', 'В процессе'),
        ('Done', 'Завершена'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='responsible_tickets')
    subject = models.CharField(max_length=100)
    description = models.TextField()
    urgent = models.CharField(max_length=6, choices=URGENCY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    def get_urgent_display(self):
        return dict(self.URGENCY_CHOICES).get(self.urgent, self.urgent)

    def get_status_display(self):
        return dict(self.STATUS_CHOICES).get(self.status, self.status)
