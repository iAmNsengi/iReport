from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from urllib.parse import urlparse, parse_qs
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import MarkForm



class HomePage(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'index.html')
    
class Dashboard(LoginRequiredMixin,View):
    def get(self,request):
        logged_in_user = User.objects.filter(username = request.user).first()
        myStudents = Student.objects.filter(creator = logged_in_user).all()
        my_classes = TheClass.objects.filter(creator = logged_in_user).all()
        my_courses = Course.objects.filter(creator = logged_in_user).all()

        context ={
            "my_students":myStudents,
            'my_classes':my_classes,
            'my_courses':my_courses,
        }
        return render(request,'dashboard.html',context)

@login_required
def AddStudent(request):
            if request.method =='POST':
                student_id = request.POST.get('student_id')
                fname = request.POST.get('fname')
                lname = request.POST.get('lname') 
                current_class = request.POST.get('current_class')
            
                if current_class:
                    try:
                        class_exist = TheClass.objects.get(code = current_class)
                        logged_in_user = User.objects.get(username = request.user)
                        new_student = Student(creator=logged_in_user,student_id=student_id,first_name=fname,last_name=lname,current_class=class_exist)
                        new_student.save()
                        messages.success(request,'Student registered successfully!')
                        return redirect('/dashboard') 
                    
                    except Exception as e:
                        messages.error(request,e)
                        return redirect('/dashboard')
                messages.error(request,'Data not found')
            return redirect('/dashboard')

@login_required
def AddCourse(request):
    if request.method =='POST':
                name = request.POST.get('name')
                code = request.POST.get('code') 

                try:
                        class_exist = Course.objects.get(code = code, title = name)
                        messages.error(request,'Course already exist!')
                        return redirect('/dashboard/')                        
                    
                except:
                        logged_in_user = User.objects.get(username = request.user)
                        new_course = Course(creator=logged_in_user,title=name,code=code)
                        new_course.save()
                        messages.success(request,'Course added successfully!')
                        return redirect('/dashboard/') 
    return redirect('/dashboard')

@login_required
def AddClass(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')
        course_ids = request.POST.getlist('courses')

        try:
            class_exist = TheClass.objects.get(code=code)
            messages.error(request, 'Class with this code already exists!')
            return redirect('/dashboard/')
        except TheClass.DoesNotExist:
            logged_in_user = User.objects.get(username=request.user)
            new_class = TheClass(creator=logged_in_user, name=name, code=code)
            new_class.save()

            for course_id in course_ids:
                course = Course.objects.get(id=course_id)
                new_class.courses.add(course)

            new_class.save()
            messages.success(request, 'Class added successfully!')
            return redirect('/dashboard/')
    return redirect('/dashboard/')


@login_required
def add_marks(request):
    if request.method == 'POST':
        form = MarkForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marks added successfully!')
            return redirect('/dashboard')
        else: 
            messages.error(request, 'Error in form submission')
    else:
        form = MarkForm(user=request.user)
    
    return render(request, 'add_marks.html', {'form': form})

class StudentReport(LoginRequiredMixin, View):
    def get(self, request, student_id):
        student = Student.objects.get(id=student_id)
        data_records = Data.objects.filter(student=student)
        courses = student.current_class.courses.all()

        context = {
            'student': student,
            'data_records': data_records,
            'courses': courses,
        }
        return render(request, 'student_report.html', context)



class Login(View):
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next', request.GET.get('next', '/'))
                netloc = urlparse(next_url).netloc
                if netloc: 
                    next_url = '/'  
                return redirect(next_url)
            else:
                messages.error(request,'404 ---- User With Given Credentials Was not found!')
                return render(request, 'login.html')
    

class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        if request.method == "POST":
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')

            try:
                User.objects.get(username = username)
                messages.error(request,f'User already exist!\nTry to signin!')
                return redirect('/signup')
            except Exception as e:
                try:
                    user = User.objects.create_user(username=username,password=password,email=email,first_name=fname,last_name=lname)
                    user.save()
                    messages.success(request,'User Created Successfully!')
                    return redirect('/login')
                except Exception as e:
                    messages.error(request,e)
                    return redirect('/signup')
    
def Logout(request):
    logout(request)
    return redirect('/login')
    