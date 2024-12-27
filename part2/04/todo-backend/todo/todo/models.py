from django.db import models

class Todo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    txt = models.CharField(max_length=255)