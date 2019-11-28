from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import NoteSerializer
from ..models import Note, Category
from datetime import datetime


class NoteListView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if request.POST['order_by'] != '':
            order_name = request.POST['order_by']
            queryset = queryset.order_by(order_name)
        if request.POST['ascending'] == 'false':
            queryset = queryset.reverse()

        if request.POST['filter_title'] != '':
            queryset = queryset.filter(title__icontains=request.POST['filter_title'])
        if request.POST['filter_category'] != '':
            queryset = queryset.filter(category=request.POST['filter_category'])
        if request.POST['elect'] != '':
            if request.POST['elect'] == 'true':
                elect = True
            else:
                elect = False
            queryset = queryset.filter(elect=elect)
        if request.POST['filter_created'] != '':
            date = datetime.strptime(request.POST['filter_created'], '%m/%d/%Y')
            queryset = queryset.filter(created__date=date)
        serializer = NoteSerializer(queryset, many=True)
        result = {'status': 'ok', 'data': serializer.data}
        return Response(result)


class NoteElectView(APIView):
    def post(self, request, *args, **kwargs):
        note_id = request.POST['id']
        if note_id:
            note = get_object_or_404(Note, id=note_id)
            note.elect = not note.elect
            note.save()
            return Response({'status': 'ok'})


class NoteDeleteView(APIView):
    def post(self, request, *args, **kwargs):
        note_id = request.POST['id']
        if note_id:
            note = get_object_or_404(Note, id=note_id)
            note.delete()
            return Response({'status': 'ok'})
