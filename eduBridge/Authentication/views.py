from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import registerStudentForm
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.http import HttpResponse

def home(request):
    obj = User.objects.all()

    ctx={
        "obj":obj
    }
    return render(request, 'Authentication/home.html',ctx)
    

def register(request):
     form = registerStudentForm()
     if request.method =='POST':
          form = registerStudentForm(request.POST)
          if form.is_valid:
               form.save()
               return redirect('login')
          else:
               return HttpResponse('Request not found')

     return render(request, 'Authentication/register.html', {'form':form} )

def loginView(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "user not found")

        user= authenticate(request, username= username, password=password)

        if user != None:
            login(request,user)
            return redirect('home')
    return render(request, 'Authentication/login.html')

def logoutView(request):
    logout(request)
    return redirect('login')