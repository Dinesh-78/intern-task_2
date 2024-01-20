from django.shortcuts import render, redirect,HttpResponseRedirect
from .forms import SignUpForm, LoginForm,AddPost
from django.contrib.auth import authenticate, login
# Create your views here.
from . models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView
from .models import blog


def index(request):
    return render(request, 'index.html')


def registerpage(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('loginpage')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def loginpage(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.doctor:
                login(request, user)
                return redirect('doctorpage')
            elif user is not None and user.patient:
                login(request, user)
                return redirect('patientpage')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})



def doctorpage(request):
    return render(request,'doctor_home.html')


def patientpage(request):
    return render(request,'patient_home.html')
@login_required
def MyProfile(request):
    user_info=User.objects.all()
    print(user_info[''])
    return render(request,'my_profile.html',{'user_info': user_info})

# class Homeview(ListView):
#     model=blog
#     template_name='blogs.html'
def myblogs(request):
    pos=blog.objects.all()
    pos=blog.objects.filter(draft=False)
    return render(request,'blogs.html',{'pos':pos})

def add_blog(request):
    msg = None
    if request.method == "POST":
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the blog model
            form.save()
            # Redirect to a new URL or modify as needed
            return HttpResponseRedirect("/tblog/")
    else:
        form = AddPost()

    return render(request, "wblog.html", {"form": form,'msg': msg})

