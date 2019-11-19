from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import NoteForm


class NoteListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account:login')
    model = Note
    template_name = 'notes/list.html'

    def get_queryset(self):
        queryset = Note.objects.filter(owner=self.request.user)
        return queryset


class NoteCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('account:login')
    form_class = NoteForm
    template_name = 'notes/create.html'
    success_url = reverse_lazy('notes:note_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(NoteCreateView, self).form_valid(form)

