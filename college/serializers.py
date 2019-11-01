from rest_framework import serializers
from .models import Student, Score, Professor


class StudentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name')


class ProfessorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('id', 'name')


class ScorePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'name', 'professor', 'student', 'value')