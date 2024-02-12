from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.

def index(request):
    return redirect('developers')

def projects(request):
    search_query = ""
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tags.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(tags__in=tags) |
        Q(owner__name__icontains=search_query)
    )
    context = {
        "projects": projects
    }
    return render(request, 'projects.html', context=context)

def singleproject(request, pk):
    project = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.owner = request.user.profile
        review.project = project
        review.save()
        return redirect('single_project', pk=project.id)
    votes = Reviews.objects.filter(project=project)
    len_votes = len(votes)
    count = 0
    context = {
        'project': project,
        'form': form,
        'votes': len_votes,

    }
    if len_votes != 0:
        count = 0
        for vote in votes:
            if vote.body == 'like':
                count += 1
        positive_vote = 100 / len_votes * count
        context.update({'positive_vote': round(positive_vote)})
    return render(request, 'single-project.html', context)


def createproject(request):
    form = ProjectForm
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        newtags = request.POST.get('newtags').replace(',' ' ').split()
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created = Tags.objects.get_or_create(name=tag)
                project.tags.add(tag)
                messages.success(request, 'Project qoshildi')
            return redirect('account')
    context = {
        "form": form
    }
    return render(request, 'form-template.html', context=context)


def updateproject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    profile = request.user.profile
    if request.method == 'POST':
        form = ProjectForm(instance=project, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('single_project', pk=pk)
    context = {
        'form': form
    }
    return render(request, 'form-template.html', context)


def delete_project(request, pk):
    profile = request.user.profile

    project = profile.project_set.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect('account')
    context = {
        'project': project
    }
    return render(request, 'delete-project.html', context)
