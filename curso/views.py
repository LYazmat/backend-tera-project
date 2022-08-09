import imp
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CursoSerializer
from .models import Curso
from django.db.models import Q

from functools import reduce

class CursoViewSet(viewsets.ModelViewSet):

    serializer_class = CursoSerializer

    def get_queryset(self):
        # reduce(lambda x, y: x | y, [Q(name__icontains=word) for word in list]))
        queryset = Curso.objects.all()
        search = self.request.query_params.get('descricao', None)
        if search:
            queryset = queryset.filter(reduce(lambda x, y: x & y, [Q(title__icontains=word) for word in search.split(' ')]))
            print(search.split(' '))
        return queryset.prefetch_related('areas')