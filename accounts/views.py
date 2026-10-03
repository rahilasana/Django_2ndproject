from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# hum ne user register krny k liye alg se koi table(model) nhi bnaya jaisy students ka bnaya tha 
#blky django k default model user ko use kiya hai 
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        # Check duplicate username
        if User.objects.filter(username=username).exists():
            return render(request,'accounts/register.html',{"error":"Username already exists."})
         # Check password match
        if password!=confirm_password:
            return render(request,'accounts/register.html',{"error":"Passwords do not match."})
        
# create_user() securely hashes the password before saving it        
        User.objects.create_user(
                username=username,
                password=password
            )
            
        return render(request, "accounts/login.html")
        
    return render(request,"accounts/register.html")

# login view

def login_view(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(
            request,
            username=username,
            password=password
            )
        
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            return render(request,"accounts/login.html",{'error':"invalid username or password"})
        
    return render(request, "accounts/login.html") 
def logout_view(request) :
    logout(request)
    return redirect('login')
     
        
    
 # Only logged-in users can access profile   
@login_required
def profile(request):
    return render(request,"accounts/profile.html")



