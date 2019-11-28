from django.db import models
from django.contrib.auth.models import User
import uuid


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    elect = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f'Note {self.title}'
