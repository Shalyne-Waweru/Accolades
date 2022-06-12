from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# SIGNUP FUNCTION
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
  

# LOGIN FUNCTION
def login_user(request):
  '''
  View function that renders the login page and its data
  '''

  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']

    print(username)
    print(password)

    user = authenticate(request, username=username, password=password)
    print(user)

    if user is not None:
      # player, created = Profile.objects.get_or_create(user=request.user)

      login(request, user)
      messages.success(request, username + " Logged In Successfully!")
      return redirect("indexPage")

    else:
      messages.error(request, "Username or Password is Incorrect. Please Try Again!")
      return redirect("loginPage")

  return render(request,"auth/login.html", locals())


# LOGOUT FUNCTION
def logout_user(request):
  '''
  View function that logs out the user
  '''
  logout(request)
  messages.success(request,"User Logged Out Successfully!")
  
  return redirect('loginPage')


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