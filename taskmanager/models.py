# taskmanager/models.py

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.title
