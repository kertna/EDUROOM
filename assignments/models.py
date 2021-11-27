from django.db import models
from django.contrib.auth.models import User

from datetime import datetime    

# Create your models here.

class Assignment(models.Model):
    QTN_CATEGORY=(
    ('Descriptive', 'Descriptive Question'),
    ('Coding', 'Coding question'),
    ('MCQ', 'Multiple Choice Questions'), 

    )
    creator = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    code= models.IntegerField(primary_key=True, help_text="Unique Code")
    title=models.CharField(max_length=100)
    deadline= models.DateField()
    question_file= models.FileField(upload_to='questions/')
    maximum_marks=models.PositiveIntegerField()
    

class Submissions(models.Model):
    id=models.IntegerField(primary_key=True)
    code=  models.IntegerField()
    student_name= models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    solution_file=  models.FileField(upload_to='solutions/')
    marks= models.IntegerField(null=True)
    comment= models.TextField(null=True)
    is_copied= models.BooleanField(null=True)
    submission_time=models.DateField(default=datetime.now)

class AssignmentDiscussion(models.Model):
    id=models.IntegerField(primary_key=True)
    code=  models.IntegerField()
    student_name= models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    message_time=  models.DateTimeField(default=datetime.now, blank=True)
    message= models.TextField()





    