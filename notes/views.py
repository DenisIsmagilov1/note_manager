from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from django.urls import reverse_lazy


class NoteListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account:login')
    model = Note
    template_name = 'notes/list.html'

    def get_queryset(self):
        queryset = Note.objects.filter(owner=self.request.user)
        return queryset

