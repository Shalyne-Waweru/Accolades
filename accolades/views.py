from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.
def landingPage(request):
  '''
  View function that renders the landing page and its information
  '''
  return render(request, "landingPage.html")

def index(request):
  '''
  View function that renders the index page and its data
  '''
  return render(request,"index.html")

def profile(request):
   '''
   View function that renders the profile page and its data
   '''
   return render(request,"profile.html")

def singleProject(request):
   '''
   View function that renders a single project page and its data
   '''
   return render(request,"single.html")

def login_user(request):
  '''
  View function that renders the login page and its data
  '''
  return render(request,"auth/login.html")

def signup_user(request):
  '''
  View function that renders the signup page and its data
  '''
  signupForm = SignUpForm()

  if request.method == "POST":
    signupForm = SignUpForm(request.POST)

    if signupForm.is_valid():
      username = signupForm.cleaned_data['username']
      
      signupForm.save()

      print(username + " Has been Saved")

      messages.success(request, username + " Registered Successfully!")
      return redirect("loginPage")
   
    else:
      messages.error(request, "Password Doesn't Meet the Requirements, Please Try Again!")
      return redirect("signupPage")    
  
  else:
    signupForm = SignUpForm()

  return render(request,"auth/signup.html", locals())