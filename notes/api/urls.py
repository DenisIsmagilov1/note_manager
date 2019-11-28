from django.urls import path
from . import views


app_name = 'notes'


urlpatterns = [
    path('list/', views.NoteListView.as_view(), name='note_list'),
    path('elect/', views.NoteElectView.as_view(), name='note_elect'),
    path('delete/', views.NoteDeleteView.as_view(), name='note_delete')
]
