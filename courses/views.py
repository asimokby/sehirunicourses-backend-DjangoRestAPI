from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Course,Exam
import datetime
from rest_framework import viewsets 
from .serializers import * 


class CoursesViewSet(viewsets.ReadOnlyModelViewSet):
        queryset = Course.objects.all()
        serializer_class = CourseSerializer

class ExamViewSet(viewsets.ReadOnlyModelViewSet):
        serializer_class = ExamSerializer
        def get_queryset(self):
                course_id  =  self.kwargs['course_id']
                queryset = Course.objects.get(pk=course_id).exam_set.all()
                return queryset
class NoteViewSet(viewsets.ReadOnlyModelViewSet):
        serializer_class = NoteSerializer
        def get_queryset(self):
                course_id  =  self.kwargs['course_id']
                queryset = Course.objects.get(pk=course_id).note_set.all()
                return queryset

class AssignmentViewSet(viewsets.ReadOnlyModelViewSet):
        serializer_class = AssignmentSerializer
        def get_queryset(self):
                course_id  =  self.kwargs['course_id']
                queryset = Course.objects.get(pk=course_id).assignment_set.all()
                return queryset
        
class QuizViewSet(viewsets.ReadOnlyModelViewSet):
        serializer_class = QuizSerializer
        def get_queryset(self):
                course_id  =  self.kwargs['course_id']
                queryset = Course.objects.get(pk=course_id).quiz_set.all()
                return queryset

class practiseViewSet(viewsets.ReadOnlyModelViewSet):
        serializer_class = PractiseSerializer
        def get_queryset(self):
                course_id  =  self.kwargs['course_id']
                queryset = Course.objects.get(pk=course_id).practise_set.all()
                return queryset



