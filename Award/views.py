from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Award.models import *
from .forms import *
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
