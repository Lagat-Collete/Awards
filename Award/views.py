from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from Award.models import *
from .forms import *
import datetime 
from .email import send_welcome_email
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
# Create your views here.

def time(request):
    datetime.datetime.now()
    return render(request,'project.html')

@login_required
def profile(request,username):
    user = request.user
    user = User.objects.filter(username=user.username).first()
    projects = Project.objects.filter(developer=user)
    return render(request, 'profile.html', {'user': user,'projects':projects})

@login_required
def user_profile(request,username):
    user = User.objects.filter(username=username).first()
    if user == request.user:
        return redirect('profile',username = user.username)
    profile = get_object_or_404(Profile,id = user.id)
    projects = Project.objects.filter(developer=user)
    return render(request, 'userprofile.html', {'user': user,'profile':profile,'projects':projects})

@login_required
def edit_profile(request,username):
    user = request.user
    user = User.objects.filter(username=user.username).first()
    profile = get_object_or_404(Profile,user=user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profileform = form.save(commit=False)
            profileform.user = user
            profileform.save()
        return redirect('profile',username = user.username)
           
    else:
        form = EditProfileForm()
    
    return render(request, 'edit_profile.html', {'form':form, 'user': user})


def project(request):
   if request.method == 'POST':
      current_user = request.user
      form = ProjectForm(request.POST, request.FILES)
      if form.is_valid():
         project = form.save(commit=False)
         project.user = current_user
         project.save()

   form = ProjectForm()
   project = Project.objects.all()
   return render(request, 'project.html', {'project':project,'form': form})

def search_results(request):

   if 'project' in request.GET and request.GET["project"]:
      search_term = request.GET.get("project")
      searched_projects = Project.search_by_title(search_term)
      message = f"{search_term}"
      form = ProjectForm()

      return render(request, 'search.html',{"message":message, "projects": searched_projects, 'form': form })
   else:
       form = ProjectForm()
       message = "You haven't searched for any term"
       return render(request, 'search.html',{"message":message, 'form': form})



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
@login_required
def project_rating(request, project_id):
    project = Project.objects.get(pk=project_id)
    ratings = Rating.objects.filter(user=request.user, project=project).first()
    rating_status = None
    username = request.user.username
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = project
            rate.save()
            project_ratings = Rating.objects.filter(project=project)

            design_ratings = [d.design for d in project_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [us.usability for us in project_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in project_ratings]
            content_average = sum(content_ratings) / len(content_ratings)

            score = (design_average + usability_average + content_average) / 3
            print(score)
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingsForm()
    
    return render(request,'rating.html', locals())

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out Sucessfully!")	

    return redirect('homepage')

def register(request):
    if request.method == 'POST':
        
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            send_welcome_email(username,email)
            
            authenticate and login 
            user = authenticate(username = username, password=password)
            login(request,user)
            return redirect('homepage')
            
    else:
        form = RegisterUserForm()
        
    return render(request,'registration/registration_form.html', {'form':form})
@login_required
def post(request):
    if request.method == 'POST':
      current_user = request.user
      form = PostForm(request.POST, request.FILES)
      if form.is_valid():
          post = form.save(commit=False)
          post.developer = current_user
          post.save()
      return redirect('homepage')
          
    else:
        form = PostForm()
        
    return render(request,'post.html', {'form':form})
