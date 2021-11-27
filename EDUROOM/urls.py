"""OnlineGrader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from assignments import views as assignment_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',assignment_views.home,name="home"),
    path('grade/<int:id>',assignment_views.grade,name="grade"),
    path('gradeAssignments/',assignment_views.getCreatedAssignments,name="gradeAssignments"),
    path('submit-message/<int:id>',assignment_views.submitMessage,name="submit-message"),
    path('check_plagiarism/<int:id>',assignment_views.checkPlagiarism,name="check_plagiarism"),
    path('register/',assignment_views.register,name="register"),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="assignments/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="assignments/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="assignments/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="assignments/password_reset_done.html"), 
        name="password_reset_complete"),

    path('create/',assignment_views.createAssignment,name="create"),
    path('search_assignment/',assignment_views.searchAssignment,name="search_assignment"),
    path('assignment_detail_for_student/',assignment_views.assignmentDetailStudent,name="assignment_detail_for_student"),
    path('accounts/profile/',assignment_views.home,name="profile"),
    path('mysubmissions/',assignment_views.getSubmittedAssignments,name="mysubmissions"),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='assignments/login.html'),name="login"),
    path('accounts/logout/',auth_views.LogoutView.as_view(template_name='assignments/logout.html'),name="logout"),
    path('assignment/<int:id>', assignment_views.assignmentDetail, name='assignment_detail'),
    path('submission-detial/<int:id>', assignment_views.submissionDetail, name='submission-detail'),
    
]

urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)