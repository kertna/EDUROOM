from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Assignment, Submissions, AssignmentDiscussion
from .forms import CreateUserForm, AssignmentForm, SubmissionForm

from pysimilar import compare
import pysimilar
import requests
import os
import glob
import datetime

from PyPDF2 import PdfFileReader
from pdfminer import high_level


# Create your views here.
def home(request):
    return render(request,'assignments/index.html')
def register(request):
    form = CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('home')
       
    context={
        'form':form
    }
    return render(request,'assignments/register.html',context)
def profile(request):
    return render(request,'assignments/profile.html')

@login_required
def createAssignment(request):
    form= AssignmentForm(creator=request.user)
    if request.method=="POST":
        form=AssignmentForm(request.POST, request.FILES,creator=request.user)
        if form.is_valid():
            form.save()
            code=form.cleaned_data.get('code')
            messages.success(request,f'Created Assignment {code}')
            return redirect('home')
       
    context={
        'form':form
    }
    return render(request,'assignments/create_assignment.html',context)

@login_required
def submitAssignment(request):
    form= SubmissionForm(student_name=request.user)
    if request.method=="POST":
        form=SubmissionForm(request.POST, request.FILES,student_name=request.user)
        if form.is_valid():
            form.save()
            
            messages.success(request,f'Submitted Successfully')
            return redirect('home')
       
    context={
        'form':form
    }
    return render(request,'assignments/assignment_detail_for_student.html',context)

@login_required
def getSubmittedAssignments(request):
    assigns= Submissions.objects.filter(student_name=request.user)
    context={
        'assigns':assigns
    }
    return render(request,'assignments/mysubmissions.html',context)
@login_required
def getCreatedAssignments(request):
    assigns= Assignment.objects.filter(creator=request.user)
    context={
        'assigns':assigns
    }
    return render(request,'assignments/myassignments.html',context)

@login_required
def checkPlagiarism(request,id):
    assign= Assignment.objects.get(code=id)
    submissions= Submissions.objects.filter(code=id)
    messages= AssignmentDiscussion.objects.filter(code=id).order_by('message_time')
    context={
        'assign':assign,
        'submissions':submissions,
        'messages':messages
    }
    
    for first in range(len(submissions)):
        for second in range(first+1, len(submissions)):
            path_to_first= 'media/'+ str(submissions[first].solution_file)
            path_to_second= 'media/'+ str(submissions[second].solution_file)
            if not path_to_first.endswith(".pdf") or not path_to_second.endswith(".pdf"):
                break
            pdffileobj1=open(path_to_first,'rb')
            pdfreader1=PdfFileReader(pdffileobj1)
            pdffileobj2=open(path_to_second,'rb')
            pdfreader2=PdfFileReader(pdffileobj2)
            numberOfPages1=pdfreader1.numPages
            numberOfPages2=pdfreader2.numPages
            pages1 = [i for i in range(numberOfPages1)]
            pages2 = [i for i in range(numberOfPages2)]
            extracted_text_first = high_level.extract_text(path_to_first, "", pages1)
            extracted_text_second = high_level.extract_text(path_to_second, "", pages2)
            
    
            if compare(extracted_text_first, extracted_text_second) >=0.9:
                submissions[first].is_copied=True
                submissions[first].save()
                submissions[second].is_copied=True
                submissions[second].save()
    return render(request,'assignments/assignment_detail.html',context)
@login_required
def assignmentDetail(request,id):
    
    assign= Assignment.objects.get(code=id)
    submissions= Submissions.objects.filter(code=id)
    messages= AssignmentDiscussion.objects.filter(code=id).order_by('message_time')
    context={
        'assign':assign,
        'submissions':submissions,
        'messages':messages
    }
    return render(request,'assignments/assignment_detail.html',context)

@login_required
def searchAssignment(request):
    return render(request,'assignments/search_assignments.html')

@login_required
def grade(request,id):
    query=request.GET.get('marks')
    submission= Submissions.objects.get(id=id)
    submission.marks=query
    submission.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def submitMessage(request,id):
    query=request.GET.get('message')
    new_message= AssignmentDiscussion(code=id, student_name= request.user,message=query)
    new_message.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
@login_required
def assignmentDetailStudent(request):
    
    query=request.GET.get('code_value')

    assign=None
    if query:
        assign = Assignment.objects.filter(code=query)
    if not assign:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if query:
        assign = Assignment.objects.get(code=query)
    
    form= SubmissionForm(student_name=request.user,code=query)
    if request.method=="POST":
        form=SubmissionForm(request.POST, request.FILES,student_name=request.user,code=query)
        if form.is_valid():
            form.save()
            
            messages.success(request,f'Submitted Successfully')
            return redirect('home')
    submission= Submissions.objects.filter(code=query, student_name=request.user)
    if submission:
        completed=True
        submission= Submissions.objects.get(code=query, student_name=request.user)
        marks=submission.marks
    else:
        completed=False
        marks=0
    msgs= AssignmentDiscussion.objects.filter(code=query).order_by('message_time')
    context={
        'assign' : assign,
        'form':form,
        'completed':completed,
        'marks':marks,
        'msgs':msgs
    }
    return render(request,'assignments/assignment_detail_for_student.html',context)
   



@login_required
def submissionDetail(request,id):
    assign = Assignment.objects.get(code=id)
    submission= Submissions.objects.get(code=id, student_name=request.user)
    msgs= AssignmentDiscussion.objects.filter(code=id).order_by('message_time')
    if submission:
        completed=True
        submission= Submissions.objects.get(code=id, student_name=request.user)
        marks=submission.marks
    else:
        completed=False
        marks=0

    context={
        'assign' : assign,
        'completed':completed,
        'marks':marks,
        'msgs':msgs
    }
    return render(request,'assignments/submission_detail.html',context)
   

