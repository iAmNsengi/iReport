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

# Create your views here.
class HomePage(LoginRequiredMixin,View):
    def get(self,request):
        
        return render(request,'index.html')
    
class Dashboard(LoginRequiredMixin,View):
    def get(self,request):
    
        return render(request,'dashboard.html')

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
                return redirect('/')
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
    