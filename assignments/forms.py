from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from django import forms

from assignments.models import Assignment, Submissions

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['code', 'title', 'deadline', 'question_file','maximum_marks']
        widgets = {
            'deadline': widgets.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('creator')
        super(AssignmentForm, self).__init__(*args,**kwargs)

    def save(self, commit=True):
        inst = super(AssignmentForm, self).save(commit=False)
        inst.creator = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst

class SubmissionForm(ModelForm):
    class Meta:
        model = Submissions
        fields = ["solution_file","comment"]
        

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('student_name')
        self._code = kwargs.pop('code')
        super(SubmissionForm, self).__init__(*args,**kwargs)

    def save(self, commit=True):
        inst = super(SubmissionForm, self).save(commit=False)
        inst.student_name = self._user
        inst.code = self._code
        if commit:
            inst.save()
            self.save_m2m()
        return inst