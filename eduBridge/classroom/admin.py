from django.contrib import admin
from .models import Course, Assignments,Submission,Enrollment,Lessons,Module

# Register your models here.
admin.site.register(Course)
admin.site.register(Assignments)
admin.site.register(Submission)
admin.site.register(Enrollment)
admin.site.register(Lessons)
admin.site.register(Module)