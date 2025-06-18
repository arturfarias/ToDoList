from django.db import models

class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7)
