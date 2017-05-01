from __future__ import unicode_literals
from datetime import datetime
from django.db import models
# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=200)
    text = models.TextField()
    due_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    