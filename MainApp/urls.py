from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view()),
    path('dashboard/', Dashboard.as_view()),
    path('add-student/',AddStudent),
    path('add-course/',AddCourse),
    path('student_report/<int:student_id>/', StudentReport.as_view(), name='student_report'),
    path('login/', Login.as_view()),
    path('signup/', Signup.as_view()),
    path('logout/', Logout),
]