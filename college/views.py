from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentPostSerializer, ProfessorPostSerializer, ScorePostSerializer
from .models import Student, Score, Professor


# Create your views here.

class StudentPostView(viewsets.ModelViewSet):
    serializer_class = StudentPostSerializer
    queryset = Student.objects.all()


class ProfessorPostView(viewsets.ModelViewSet):
    serializer_class = ProfessorPostSerializer
    queryset = Professor.objects.all()


class ScorePostView(viewsets.ModelViewSet):
    serializer_class = ScorePostSerializer
    queryset = Score.objects.all()