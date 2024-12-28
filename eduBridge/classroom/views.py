from django.shortcuts import render,get_object_or_404,redirect
from .models import Course,Assignments,Submission,Enrollment,Lessons,Module
from .forms import AssignmentsForm,SubmissionForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.http.response import HttpResponse

def homeView(request):
    course =Course.objects.all()
   
    return render(request, 'classroom/index.html',{'courses':course} )


def course(request):
    course = Course.objects.all()
    context ={
        'courses':course
    }
    return render(request, 'classroom/courses.html', context)

def detailCourse(request,course_id):
    course =get_object_or_404(Course, id=course_id)
    lessons = course.lessons.all().order_by('order')
    modules = course.modules.all().order_by('order')
    user = request.user

    context={
        'course': course,
        'lessons': lessons,
        'modules': modules,
        'user':user
    }
    return render(request, 'classroom/course-detail.html', context)


def profile(request,username):
    user = User.objects.all()
    profile = get_object_or_404(user, username=username)

    return render(request, 'classroom/profile.html',{'profiles':profile})

def post_AssignmentView(request):
    if request.method == 'POST':
        form = AssignmentsForm(request.POST)
        if form.is_valid():
            assignment=form.save(commit=False)
            assignment.instructor=request.user
            assignment.save()
            return redirect('assignments')
    else:
        form = AssignmentsForm()
    return render(request, 'classroom/post-assignment.html', {'form':form})

def Assignment_list(request):
    if request.user.is_staff:
        assignments = Assignments.objects.filter(instructor=request.user)
    else:
        assignments = Assignments.objects.all()

    return render(request, 'classroom/assignments.html', {'assignments':assignments})


def submit_Assignment(request,assignment_id):
    assignment = get_object_or_404(Assignments, id=assignment_id)

    if request.method=='POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.student=request.user
            instance.assignment=assignment
            instance.save()
            return redirect('assignments')
    else:
        form=SubmissionForm()
    return render(request, 'classroom/submit-assignment.html',{'form':form, 'assignment':assignment} )


def  Submission_list(request):
    submission = Submission.objects.all()
    
    return render(request, 'classroom/submission_list.html', {"submissions":submission})


def grade(request,submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    if request.method == 'POST':
        submission.grade = request.POST.get('grade')
        submission.feedback =  request.POST.get('feedback')
        submission.graded = True
        submission.save()
        return redirect('submission_list')  
    return render(request, 'classroom/grade.html', {'submission': submission})

def enrollment(request,course_id):
    course = get_object_or_404(Course, id=course_id)

    if Enrollment.objects.filter(user = request.user, course=course).exists():
            messages.warning(request, 'You are already enrolled in this course')
    else:
        try:
            Enrollment.objects.create(user=request.user, course=course)
            messages.success(request, 'you have successfully enrolled')
        except exception as e:
            return HttpResponse('An error occured')

    return redirect('course-detail',course_id=course.id)

