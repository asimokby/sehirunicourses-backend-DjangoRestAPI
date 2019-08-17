from rest_framework import serializers 
from .models import Course, Exam, Note, Assignment, Quiz, Practise


class CourseSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Course
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Exam
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class PractiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practise
        fields = '__all__'