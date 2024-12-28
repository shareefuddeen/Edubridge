from django.urls import path
from . import views



urlpatterns =[
    path('home/', views.homeView, name='home'),
    path('courses/', views.course, name='courses'),
    path('course-detail/<str:course_id>/',views.detailCourse, name='course-detail'),
    path('course/<str:course_id>/enroll/', views.enrollment, name='enroll'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('post-assignment/',views.post_AssignmentView, name='create-assignment'),
    path('assignments/',views.Assignment_list, name='assignments'),
    path('submit-assignment/<int:assignment_id>/', views.submit_Assignment, name='submit-assignment'),
    path('submissions/',views.Submission_list, name="submission_list"),
    path('submission/<int:submission_id>/grade/', views.grade, name="grade")
]   