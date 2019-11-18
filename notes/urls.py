from django.urls import path
from . import views


app_name = 'notes'

urlpatterns = [
    path('list/', views.NoteListView.as_view(), name='note_list')
]
