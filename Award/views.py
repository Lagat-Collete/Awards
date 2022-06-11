from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Award.models import *
from .forms import *
import datetime as dt
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
# Create your views here.

def home_page(request):
   return render(request,'homepage.html')

def project(request):
   current_user = request.user
   if request.method == 'POST':
      form = ProjectForm(request.POST, request.FILES)
      if form.is_valid():
         project = form.save(commit=False)
         project.developer = current_user
         project.save()

   form = ProjectForm()
   return render(request, 'project.html', {'form': form})

def search_results(request):

   if 'project' in request.GET and request.GET["project"]:
      search_term = request.GET.get("project")
      searched_projects = Project.search_by_title(search_term)
      message = f"{search_term}"

      return render(request, 'search.html',{"message":message, "projects": searched_projects})
   else:
       message = "You haven't searched for any term"
       return render(request, 'search.html',{"message":message})

def rating(request):
   obj =Rating.objects.filter(usability=0).order_by("?").first()
   context ={
      'object': obj
   }
   return render(request, 'ratings.html', context)

class ProfileList(APIView):
   def get(self, request, format=None):
      all_profile = Profile.objects.all()
      serializers = ProfileSerializer(all_profile, many=True)
      return Response(serializers.data)


class ProjectList(APIView):
   def get(self, request, format=None):
      all_project = Project.objects.all()
      serializers = ProjectSerializer(all_project, mant=True)
      return Response(serializers.data)
