from django.db import models

# Create your models here.
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

    subject = models.CharField(max_length=100)
    description = models.TextField()
    urgent = models.CharField(max_length=6, choices=URGENCY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject