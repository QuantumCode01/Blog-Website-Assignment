from django.shortcuts import render,redirect
from .forms import UserRegisterationForm,UserAuthenticationForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.
def signupform(request):
    fm=UserRegisterationForm()
    if request.method=="POST":
        fm=UserRegisterationForm(request.POST)
       
        if fm.is_valid():
            messages.success(request,'Account Created Successfully.....')
            fm.save()
           
            return redirect('/')
        else:
            return render(request,'app/signup.html',{'form':fm})
    return render(request,'app/signup.html',{'form':fm})

def userlogin(request):
    # if user is not logged in then if statement is true and code inside it runs 
    if not request.user.is_authenticated:
        if request.method =="POST":
            fm=UserAuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                usname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=usname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Logged in Successfullly!!!!')   
                    return HttpResponseRedirect('/')
        else:
            fm=UserAuthenticationForm()
            return render(request,'app/login.html',{'form':fm})
    # if user loggedin then user will be redirected to the home page or events.html template
    else:
        return redirect('/')
    
@login_required(login_url='/login/')   
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')


def post(request):
    data=Post.objects.all()
    return render(request,'app/home.html',{'post':data})

@login_required(login_url='/login/')
def createpost(request):
    if request.method =="POST":
        fm=PostForm(request.POST,request.FILES)
        if fm.is_valid():
            title=  fm.cleaned_data['title']
            content=  fm.cleaned_data['content']
            image = fm.cleaned_data['image']
            reg=Post(name=request.user,title=title,content=content,image=image)
            reg.save()
            messages.success(request,"Post Created Successfully!!")
            return  redirect('/')
    else:
        fm=PostForm()
    return render(request,'app/createpost.html',{'form':fm})


@login_required(login_url='/login/')
def userposts(request):
    if request.user.is_authenticated:
        pt=Post.objects.filter(name=request.user)
        print(request.user)
        return render(request,'app/userposts.html',{'post':pt})

 
def postdetails(request,pk):
    data=Post.objects.get(id=pk)
    print(data)
    return render(request,'app/postdetails.html',{'post':data})