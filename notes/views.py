from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note


class NoteListView(ListView):
    model = Note
    template_name = 'notes/list.html'

