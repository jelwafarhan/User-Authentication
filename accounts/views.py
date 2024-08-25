from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout 
# Create your views here.





def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
         login(request, user)
         return redirect('home')
        else:
             error_massage='invalid=username or password'
    else:
        error_massage=None
        return render(request,'accounts/login.html',{'error_massage':error_massage})
    
def home(request):
    return render(request,'accounts/home.html',{'username':request.user.username})

from .forms import UserRegistrationform

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

            
            
    else:
        form = UserRegistrationform()
    return render(request,'accounts/registration.html',{'form':form})

    

def logout_user(request):
    logout(request)
    return redirect('login')