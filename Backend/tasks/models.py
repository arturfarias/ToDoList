from django.db import models
from django.contrib.auth.models import User

from tags.models import Tag

class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)


class Topic(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='topics')
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
