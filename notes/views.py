from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import NoteForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404


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


class NoteDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('account:login')
    model = Note
    template_name = 'notes/detail.html'


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('account:login')
    model = Note
    form_class = NoteForm
    template_name = 'notes/update.html'
    success_url = reverse_lazy('notes:note_list')


@login_required
@require_POST
def note_elect(request):
    note_id = request.POST['id']
    if note_id:
        note = get_object_or_404(Note, id=note_id)
        note.elect = not note.elect
        note.save()
        return JsonResponse({'status': 'ok'})
