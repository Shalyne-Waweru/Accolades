from django.shortcuts import render

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