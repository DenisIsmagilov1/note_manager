from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    CATEGORIES = (
        ('L', 'Link'),
        ('N', 'Note'),
        ('M', 'Memo'),
        ('D', 'TODO')
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=1, choices=CATEGORIES, default='N')
    elect = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f'Note {self.title}'
