from django.shortcuts import render

# Create your views here.
def landingPage(request):
  '''
  View function that renders the landing page and its information
  '''
  return render(request, "landingPage.html", {})
