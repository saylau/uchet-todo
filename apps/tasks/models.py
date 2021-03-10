from django.db import models

from apps.users.models import User

from .managers import TaskQueryset


class Task(models.Model):
    """
    Task model
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_to = models.DateTimeField(null=True)
    is_done = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    objects = TaskQueryset.as_manager()

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"
