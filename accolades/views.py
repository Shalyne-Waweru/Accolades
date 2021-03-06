from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .serializer import ProjectSerializer, ProfileSerializer
from django.contrib.auth.decorators import login_required

# DJANGO REST_FRAMEWORK
from rest_framework.decorators import api_view
from rest_framework.response import Response

# LANDING PAGE FUNCTION
def landingPage(request):
  '''
  View function that renders the landing page and its information
  '''
  return render(request, "landingPage.html")

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


# PROFILE FUNCTION
@login_required(login_url='/login')
def profile(request, username):
   '''
   View function that renders the profile page and its data
   '''

   # Query the database to get the username of the user
   user_profile = get_object_or_404(User, username=username)

   #Query the database to get the projects of that user
   myProjects = Project.objects.filter(user = user_profile.id).all()
  
   user_info_form = UpdateUserInfoForm()
   update_profile_form = UpdateProfileForm()
   projectForm = ProjectForm()

   if request.method == 'POST':
      user_info_form = UpdateUserInfoForm(request.POST,instance=request.user)
      update_profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
      projectForm = ProjectForm(request.POST, request.FILES)

      if projectForm.is_valid():
        title = projectForm.cleaned_data['title']
        description = projectForm.cleaned_data['description']
        link = projectForm.cleaned_data['link']
        image = request.FILES['image']

        new_project = Project(user=request.user, title=title, image=image, description=description, link=link)
        new_project.save()

        print(title)
        print(description)
        print(link)
        print(image)

        messages.success(request, "Project Added Successfully!")
        return redirect("indexPage")

      elif user_info_form.is_valid() and update_profile_form.is_valid():
              
              user_info_form.save()
              update_profile_form.save()

              messages.success(request, "Profile Updated Successfully!")
              return HttpResponseRedirect(request.path_info)

      else:
        messages.error(request, "Oops, an error occured. Please Try Again!")
        return HttpResponseRedirect(request.path_info)
   
   else:
          user_info_form = UpdateUserInfoForm(instance=request.user)
          update_profile_form = UpdateProfileForm(instance=request.user.profile)
          projectForm = ProjectForm()
  
   return render(request,"profile.html", locals())


# MAIN PAGE FUNCTION
def index(req):
  '''
  View function that renders the index page and its data
  '''

  projectForm = ProjectForm()

  # Query the database for the most recent project
  recent_project = Project.objects.latest('date')
  print(recent_project)

  # Query the database for all the projects
  projects = Project.objects.all()

  if req.method == "POST":
    projectForm = ProjectForm(req.POST, req.FILES)

    if projectForm.is_valid():
      title = projectForm.cleaned_data['title']
      description = projectForm.cleaned_data['description']
      link = projectForm.cleaned_data['link']
      image = req.FILES['image']

      new_project = Project(user=req.user, title=title, image=image, description=description, link=link)
      new_project.save()

      print(title)
      print(description)
      print(link)
      print(image)

      messages.success(req, "Project Added Successfully!")
      return redirect("indexPage")
      
    else:
      messages.error(req, projectForm.errors)
      return redirect("indexPage")
    
  else:
    projectForm = ProjectForm()
  
  return render(req,"index.html", locals())


# SINGLE PROJECT FUNCTION
@login_required(login_url='/login')
def singleProject(request, id):
   '''
   View function that renders a single project page and its data
   '''

   project = Project.get_project_by_id(id)
   print(project)

   # Query the database to get all the votes of a particular project
   rates = Rates.objects.filter(project=id).all()
   print(rates)

   if request.method == "POST":
    design_rate = request.POST.get('d-rate')
    usability_rate = request.POST.get('u-rate')
    content_rate = request.POST.get('c-rate')

    print(design_rate)
    print(usability_rate)
    print(content_rate)
    print(project.id)

    new_vote = Rates(user=request.user, project=project, design_rate=design_rate, usability_rate=usability_rate, content_rate=content_rate )
    new_vote.save()
    messages.success(request, "Thanks " + request.user.username + ". Your Vote Has Been Added Successfully! ")
    return redirect(reverse('singleProjectPage', args=[id]))

   return render(request,"single.html", locals())


# SEARCH PROJECT FUNCTION
def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_project(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


# -------> API FUNCTIONS <-------- #

# GET ALL PROJECTS
@api_view(['GET'])
def getProjects(request):
  '''
  View Function that gets all the submitted projects
  '''

  # Query the database to get all the projects
  projects = Project.objects.all()

  # Serializing the Django model objects
  ser_projects = ProjectSerializer(projects, many=True)

  return Response(ser_projects.data)


# GET ALL THE USER PROFILES
@api_view(['GET'])
def getProfiles(request):
  '''
  View function that returns all the user profiles
  '''

  # Query the database to get all the profiles
  profiles = Profile.objects.all()

  # Serializing the Django model objects
  ser_profiles = ProfileSerializer(profiles, many=True)

  return Response(ser_profiles.data)




