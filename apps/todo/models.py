from django.db import models


class Todo(models.Model):
    """
    Todo model
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_to = models.DateTimeField(null=True)
    is_done = models.BooleanField(default=False)