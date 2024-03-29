from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note, Category
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import NoteForm


class NoteListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account:login')
    model = Note
    template_name = 'notes/list.html'

    def get_queryset(self):
        queryset = Note.objects.filter(owner=self.request.user)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super(NoteListView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        result['categories'] = categories
        result['order_field_names'] = ['created', 'category', 'elect']
        result['filter_field_names'] = ['created', 'title', 'category']
        return result


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
