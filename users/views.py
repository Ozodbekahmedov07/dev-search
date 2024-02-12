from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def developers(request):
    search_query = ""
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skills.objects.filter(name__icontains=search_query)
    print(skills)
    developers = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skills__in=skills)
    )
    context = {
        'developers': developers
    }

    return render(request, 'index.html', context)


def userprofile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skills_set.exclude(description__exact="")
    otherSkills = profile.skills_set.filter(description="")
    context = {
        'profile': profile,
        'topskills': topSkills,
        'otherskills': otherSkills
    }

    return render(request, 'profile.html', context)


@login_required(login_url='login')
def useraccount(request):
    profile = request.user.profile
    topSkills = profile.skills_set.exclude(description__exact="")
    otherSkills = profile.skills_set.filter(description="")
    context = {
        'profile': profile,
        'topskills': topSkills,
        'otherskills': otherSkills
    }
    return render(request, 'account.html', context)


def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Profilga xush kelibsiz')
            return redirect('account')
        else:
            messages.error(request, 'User topilmadi')
    return render(request, 'login.html')


def userregister(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            Profile.objects.create(
                user=user,
                username=user.username,
                email=user.email,
                name=user.first_name
            )
            login(request, user)
            send_mail(
                subject='Welcome! http://127.0.0.1:8000/',
                message=f"Xush kelibsiz {user.first_name}!",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False)

            send_mail(
                'Yangi foydalanuvchi! http://127.0.0.1:8000/',
                f'Ismi: {user.first_name},\n'
                f'Familiyasi: {user.last_name},\n'
                f'Email: {user.email},\n'
                f'Usename: {user.username},',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False
            )
            return redirect('account')
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)


def userlogout(request):
    logout(request)
    messages.info(request, 'Xayr')
    return redirect('developers')


def edit_account(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('account')
    form = ProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'edit-account.html', context)


def createskills(request):
    form = SkillsForm()
    if request.method == 'POST':
        form = SkillsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            skills = form.save(commit=False)
            skills.owner = request.user.profile
            skills.save()
            return redirect('account')
    context = {
        'form': form
    }
    return render(request, 'skills-form.html', context)


def editskills(request, pk):
    profile = request.user.profile
    skill = profile.skills_set.get(id=pk)
    if request.method == 'POST':
        form = SkillsForm(instance=skill, data=request.POST, files=request.FILES)
        if form.is_valid():
            skills = form.save(commit=False)
            skills.owner = request.user.profile
            skills.save()
            return redirect('account')
    form = SkillsForm(instance=skill)
    context = {
        'form': form
    }
    return render(request, 'skills-form.html', context)


def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skills_set.get(id=pk)
    if request.method == "POST":
        skill.delete()
        return redirect('account')
    context = {
        'skill': skill
    }
    return render(request, 'delete-skill.html', context)


def inbox_message(request):
    profile = request.user.profile
    inbox = profile.messages.all()
    countmesssage = inbox.filter(is_read=False).count()
    context = {
        'inbox_messages': inbox,
        'countmesssage': countmesssage
    }
    return render(request, 'inbox.html', context)

def viewmessage(request, pk):
    onemessage = Inbox.objects.get(id=pk)
    if onemessage.is_read == False:
        onemessage.is_read = True
        onemessage.save()

    context = {
        'onemessage': onemessage
    }
    return render(request, 'message.html', context)

def sendmessage(request, pk):
    profile = Profile.objects.get(id=pk)
    form = MeesageForm()
    if request.method == "POST":
        form = MeesageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user.profile
            message.recipient = profile
            message.save()
            return redirect('profile', pk=profile.id)
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'send-message.html', context)
