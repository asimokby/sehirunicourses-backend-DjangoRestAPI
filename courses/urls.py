from django.urls import path, include 
from . import views
from rest_framework import routers 
from .models import *
# from django.contrib import admin


router = routers.DefaultRouter()
router.register('courses', views.CoursesViewSet, basename= 'Course')
router.register(r'exams/(?P<course_id>.+)', views.ExamViewSet, base_name='Exam')
router.register(r'notes/(?P<course_id>.+)', views.NoteViewSet, base_name='Note')
router.register(r'assignments/(?P<course_id>.+)', views.AssignmentViewSet, base_name='Assignment')
router.register(r'quizes/(?P<course_id>.+)', views.QuizViewSet, base_name='Quiz')
router.register(r'practises/(?P<course_id>.+)', views.practiseViewSet, base_name='Practise')

app_name = 'courses'
urlpatterns = [
    path('', include(router.urls)),
]

