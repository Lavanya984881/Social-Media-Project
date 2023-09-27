from django.shortcuts import render, redirect
from .models import Image,Feedback
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse




def SignupPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'login.html')

def logout(request):
    return redirect('login')

def ArticlePage(request):
    if request.method == 'POST':
        Image(
            image=request.FILES['image'],
            article_name=request.POST.get('article'),
            description=request.POST.get('description'),
            ).save()
        return redirect('home')
    return render(request, 'article.html')

def home(request):
    data = Image.objects.all()
    return render(request, 'home.html', {'data': data})

def feedback(request):
    tata=Feedback.objects.all()
    return render(request,'feedback.html',{'tata':tata})

def addfeedback(request):
    if request.method=='GET':
        return render(request,'addfeedback.html')

    else:
        Feedback(
            name=request.POST.get('name'),
            comment=request.POST.get('feedback')
        ).save()
        return redirect('home')
