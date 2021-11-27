from django.contrib import admin

from .models import Assignment, Submissions, AssignmentDiscussion

# Register your models here.

admin.site.register(Assignment)
admin.site.register(Submissions)
admin.site.register(AssignmentDiscussion)