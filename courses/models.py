from django.db import models
from django.urls import reverse


class Course(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)
    syllabus = models.URLField(max_length=2000)


    def __str__(self):
        return self.name

class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_title = models.CharField(max_length=30)
    exam_file_q = models.URLField(max_length=2000)


class Note(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    note_title = models.CharField(max_length=30)
    note_file = models.URLField(max_length=2000)

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment_title = models.CharField(max_length=30)
    assignment_file_q =  models.URLField(max_length=2000)
    
class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quiz_title = models.CharField(max_length=30)
    quiz_file_q = models.URLField(max_length=2000)

class Practise(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    practise_title = models.CharField(max_length=30)
    parctise_file = models.URLField(max_length=2000)



