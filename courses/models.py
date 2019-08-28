from django.db import models
from django.urls import reverse


class Course(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)
    syllabus = models.FileField(upload_to='syllabus')


    def __str__(self):
        return self.name

class Exam(models.Model):
    course_name = models.CharField(max_length=20, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_title = models.CharField(max_length=30)
    exam_file_q = models.FileField(upload_to='exam_questions')


class Note(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    note_title = models.CharField(max_length=30)
    note_file = models.FileField(upload_to='notes')

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment_title = models.CharField(max_length=30)
    assignment_file_q =  models.FileField(upload_to='assignment_questions')
    
class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quiz_title = models.CharField(max_length=30)
    quiz_file_q = models.FileField(upload_to='quiz_questions')

class Practise(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    practise_title = models.CharField(max_length=30)
    parctise_file = models.FileField(upload_to='practises')



