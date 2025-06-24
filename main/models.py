from django.db import models
from django.contrib.auth.models import User



class Tasks(models.Model):
    CHOICES = (
        ('New', 'New'),
        ('In-Progress', 'In-Progress'),
        ('Completed', 'Completed'),
    )
    title = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=CHOICES, default='New')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
