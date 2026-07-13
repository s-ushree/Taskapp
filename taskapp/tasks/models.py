from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES=[
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    image=models.ImageField(upload_to='task_images/', blank=True, null=True)
    file=models.FileField(upload_to='task_files/', blank=True, null=True,)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

