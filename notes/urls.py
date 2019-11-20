from django.urls import path
from . import views


app_name = 'notes'

urlpatterns = [
    path('list/', views.NoteListView.as_view(), name='note_list'),
    path('create/', views.NoteCreateView.as_view(), name='note_create'),
    path('detail/<pk>/', views.NoteDetailView.as_view(), name='note_detail'),
    path('update/<pk>/', views.NoteUpdateView.as_view(), name='note_update')
]
