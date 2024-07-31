# gas_app/models.py

from django.db import models
from django.contrib.auth.models import User

class Request(models.Model):
    TYPE_CHOICES = [
        ('Maintenance', 'Maintenance'),
        ('Billing Issue', 'Billing Issue'),
        # Add other types as needed
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file_attachment = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return f'Request {self.id} by {self.user.username}'
