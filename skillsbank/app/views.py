from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomPasswordResetView, CustomUserCreationForm, SkillForm, SimpleSkillForm, ContactForm
from .models import Skill, Category, Profile
import json
import hashlib
from django.core.mail import send_mail
import os
from dotenv import load_dotenv
from django.conf import settings


load_dotenv()

""" Home (User Logged in)"""
@login_required
def home(request):
    context = {
        "username": request.user.username  
    }
    return render(request, 'home.html', context)


""" Index (Public)"""
def index(request):
    return render(request, 'index.html')


""" Search (Public) """
def search_users_by_skill(request):
    query = request.GET.get('search', '')  
    users_with_skills = []

    if query:
        skills_matching_query = Skill.objects.filter(name__icontains=query, user__isnull=False)


        for skill in skills_matching_query:
            if skill.user.profile.public_username:  
                users_with_skills.append(skill.user.profile.public_username)  

        users_with_skills = list(set(users_with_skills))


        total_results = len(users_with_skills)

        users_with_skills = users_with_skills[:10]

        results_message = f"There are a total of <strong class='orange-text'>{total_results} {query}</strong> in the <strong class='red-text'>Skills</strong>Bank. Here are <span class='orange-text'>{len(users_with_skills)}</span> results."


    else:
        results_message = None
        users_with_skills = []
        total_results = 0

    return render(request, 'index.html', {
        'users_with_skills': users_with_skills,
        'results_message': results_message,
        'query': query,
        'total_results': total_results,
    })

""" Terms (Public)"""
def terms(request):
    return render(request, 'terms.html')

""" Privacy (Public)"""
def privacy(request):
    return render(request, 'privacy-policy.html')

""" About (Public)"""
def about(request):
    return render(request, 'about.html')

""" Contact (Public)"""
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            try:
                from_email = os.getenv('DEFAULT_FROM_EMAIL', 'noreply@skillsbank.slammin-design.co.uk')

                recipient_list = os.getenv('EMAIL_CONTACT', '').split(',')

                send_mail(
                    subject=f"Contact Form Message from {name}",
                    message=f"From: {name} ({email})\n\nMessage:\n{message}",
                    from_email=from_email,
                    recipient_list=recipient_list,
                    fail_silently=False,
                )

                messages.success(request, "Thanks for your message. Your message was sent successfully.")
                return render(request, "contact.html", {"form": ContactForm()})  

            except Exception as e:
                messages.error(request, f"Your message was not sent. Error: {e}")

        else:
            messages.error(request, "Your message was not sent. Please check the form and try again.")

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

"""  (Public)"""
#@csrf_exempt
#@login_required
def add_quick_skill(request):
    if request.method == 'POST':
        form = SimpleSkillForm(request.POST)

        if form.is_valid():
            skill = form.save(commit=False)  
            skill.user = request.user  
            skill.save() 

            messages.success(request, 'Skill added successfully.')
            return redirect("add-quick-skill") 
    else:
        form = SimpleSkillForm()

    return render(request, 'home.html', {'form': form})


def skill_detail(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    return render(request, 'skill_detail.html', {'skill': skill})



def skills_directory(request):
    skills = Skill.objects.all()

    skills_by_category = {"Uncategorised": []} 
    skills_by_context = {}

    for skill in skills:
        categories = skill.category.all()
        if categories.exists():  
            for category in categories:
                if category.name not in skills_by_category:
                    skills_by_category[category.name] = []
                skills_by_category[category.name].append(skill)
        else:
            skills_by_category["Uncategorised"].append(skill)

    for skill in skills:
        for context in skill.context.all():  
            if context.name not in skills_by_context:
                skills_by_context[context.name] = []
            skills_by_context[context.name].append(skill)

    for skill in skills:
        skill.progress_width = skill.experience * 20  
        if skill.experience == 1:
            skill.progress_color = 'yellow'
        elif skill.experience == 2:
            skill.progress_color = 'orange'
        elif skill.experience == 3:
            skill.progress_color = 'blue'
        elif skill.experience == 4:
            skill.progress_color = 'lightgreen'
        elif skill.experience == 5:
            skill.progress_color = 'green'
        else:
            skill.progress_color = 'grey'

    for skill in skills:
        skill.proficiency_width = skill.proficiency * 20  
        if skill.proficiency == 1:
            skill.proficiency_progress_class = 'progress-yellow'
        elif skill.proficiency == 2:
            skill.proficiency_progress_class = 'progress-orange'
        elif skill.proficiency == 3:
            skill.proficiency_progress_class = 'progress-blue'
        elif skill.proficiency == 4:
            skill.proficiency_progress_class = 'progress-lightgreen'
        elif skill.proficiency == 5:
            skill.proficiency_progress_class = 'progress-green'
        else:
            skill.proficiency_progress_class = 'progress-grey'

    total_skills = len(skills)
    total_categories = len(skills_by_category)

    print("Skills grouped by category:", {'skills_by_category': skills_by_category})

    return render(request, 'skills-directory.html', {
        'skills_by_category': skills_by_category, 
        'skills_by_context': skills_by_context,
        'skills' : skills,
        'skills_count': total_skills,
        'categories_count': total_categories
    })


""" Authentication (Public)"""
# Authentication System

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

""" Logout (Public)"""
def logout_view(request):
    logout(request)
    return redirect('login')

""" Register (Public)"""
"""
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
"""

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect("home") 
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


"""  Forgot Password (Public)"""
def forgot_password_view(request):
    return CustomPasswordResetView.as_view(template_name='forgot_password.html')(request)

"""  Password Reset (Public)"""
def password_reset_view(request):
    return CustomPasswordResetView.as_view(template_name='password_reset_request.html')(request)


""" Skills """
# Main Site Content

""" Skills Table View """
@login_required
def skill_account(request):
    skills = Skill.objects.filter(user=request.user).order_by('-id')  
    return render(request, 'skills-account.html', {'skills': skills})

""" User Skills """
def user_skills(request):
    skills = Skill.objects.filter(user=request.user)

    skills_by_category = {"Uncategorised": []} 
    skills_by_context = {}

    for skill in skills:
        categories = skill.category.all()
        if categories.exists():  
            for category in categories:
                if category.name not in skills_by_category:
                    skills_by_category[category.name] = []
                skills_by_category[category.name].append(skill)
        else:
            skills_by_category["Uncategorised"].append(skill)
    

    for skill in skills:
        for context in skill.context.all():  
            if context.name not in skills_by_context:
                skills_by_context[context.name] = []
            skills_by_context[context.name].append(skill)

    for skill in skills:
        skill.progress_width = skill.experience * 20  
        if skill.experience == 1:
            skill.progress_color = 'yellow'
        elif skill.experience == 2:
            skill.progress_color = 'orange'
        elif skill.experience == 3:
            skill.progress_color = 'lightblue'
        elif skill.experience == 4:
            skill.progress_color = 'lightgreen'
        elif skill.experience == 5:
            skill.progress_color = 'green'
        else:
            skill.progress_color = 'grey'

    for skill in skills:
        skill.proficiency_width = skill.proficiency * 20  
        if skill.proficiency == 1:
            skill.proficiency_progress_color = 'yellow'
        elif skill.proficiency == 2:
            skill.proficiency_progress_color = 'orange'
        elif skill.proficiency == 3:
            skill.proficiency_progress_color = 'lightblue'
        elif skill.proficiency == 4:
            skill.proficiency_progress_color = 'lightgreen'
        elif skill.proficiency == 5:
            skill.proficiency_progress_color = 'green'
        else:
            skill.proficiency_progress_color = 'grey'

    for skill in skills:
        skill.enjoyment_width = skill.enjoyment * 20  
        if skill.enjoyment == 1:
            skill.enjoyment_progress_color = 'yellow'
        elif skill.enjoyment == 2:
            skill.enjoyment_progress_color = 'orange'
        elif skill.enjoyment == 3:
            skill.enjoyment_progress_color = 'lightblue'
        elif skill.enjoyment == 4:
            skill.enjoyment_progress_color = 'lightgreen'
        elif skill.enjoyment == 5:
            skill.enjoyment_progress_color = 'green'
        else:
            skill.enjoyment_progress_color = 'grey'

    total_skills = len(skills)
    total_categories = len(skills_by_category)


    print("Skills grouped by category:", {'skills_by_category': skills_by_category})

    return render(request, 'skills-list.html', {
        'skills_by_category': skills_by_category, 
        'skills_by_context': skills_by_context,
        'skills' : skills,
        'skills_count': total_skills,
        'categories_count': total_categories
    })




""" Create Skill """
@login_required
def create_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        form.user = request.user  # Pass the logged-in user to the form
        if form.is_valid():
            form.save()  # The form's save method will now automatically set the user
            return redirect('skill_list')  # Redirect to the skill list page
    else:
        form = SkillForm()

    return render(request, 'create_skill.html', {'form': form})


""" Add user skills """
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)

        print("Raw POST data:", request.POST)  # 🔍 Print what Django receives

        if form.is_valid():
            skill = form.save(commit=False)  # Save skill object without committing yet
            skill.user = request.user
            skill.save()  # First save (now it has an ID)

            # 🔍 Debug: Check what was selected
            context_values = form.cleaned_data.get('context', [])
            category_values = form.cleaned_data.get('category', [])

            print("Context Selected:", context_values)  # Should print selected context objects
            print("Category Selected:", category_values)  # Should print selected category objects

            skill.context.set(context_values)  
            skill.category.set(category_values)

            skill.save()  # Save again after setting ManyToMany relationships

            messages.success(request, 'Skill added successfully.')
            return redirect("add_skill")

    else:
        form = SkillForm()

    return render(request, 'add-skill.html', {'form': form})

""" Edit User Skills """
def edit_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_account')
    else:
        form = SkillForm(instance=skill)

    return render(request, 'edit-skill.html', {'form': form, 'skill': skill})


""" Delete User Skills """
def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)

    if request.method == "POST":
        skill.delete()
        return redirect('skill_account')

    return render(request, 'delete-skill.html', {'skill': skill})

""" User Profile (Personal) """
@csrf_exempt
@login_required
def user_profile(request, username):
    if request.user.username != username:
        return redirect('index')  
    
    user = get_object_or_404(User, username=username)

    email = user.email.strip().lower()
    email_hash = hashlib.md5(email.encode('utf-8')).hexdigest()
    gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}?s=200"  
    
    top_skills = Skill.objects.filter(user=user).order_by('-proficiency')[:10]
    recent_skills = Skill.objects.filter(user=user).order_by('-id')[:10]
    most_experienced_skills = Skill.objects.filter(user=user).order_by('-experience')[:5]
    most_enjoyable_skills = Skill.objects.filter(user=user).order_by('-enjoyment')[:5]
    most_proficient_skills = Skill.objects.filter(user=user).order_by('-proficiency')[:5]

    certifications = Skill.objects.filter(user=user).exclude(certification__isnull=True).exclude(certification="")

    return render(request, 'profile.html', {
        'user': user,
        'gravatar_url': gravatar_url,
        'top_skills': top_skills,
        'recent_skills': recent_skills,
        'most_experienced_skills': most_experienced_skills,
        'most_enjoyable_skills': most_enjoyable_skills,
        'most_proficient_skills': most_proficient_skills,
        'certifications': certifications,
    })


""" Public User Profile View"""
def public_user_profile(request, username):
    profile = get_object_or_404(Profile, public_username=username)

    user = profile.user

    email = user.email.strip().lower()
    email_hash = hashlib.md5(email.encode('utf-8')).hexdigest()
    gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}?s=200"  
    
    top_skills = Skill.objects.filter(user=user).order_by('-proficiency')[:10]
    recent_skills = Skill.objects.filter(user=user).order_by('-id')[:10]
    most_experienced_skills = Skill.objects.filter(user=user).order_by('-experience')[:5]
    most_enjoyable_skills = Skill.objects.filter(user=user).order_by('-enjoyment')[:5]
    most_proficient_skills = Skill.objects.filter(user=user).order_by('-proficiency')[:5]

    certifications = Skill.objects.filter(user=user).exclude(certification__isnull=True).exclude(certification="")

    return render(request, 'public.html', {
        'user': user,
        'gravatar_url': gravatar_url,
        'top_skills': top_skills,
        'recent_skills': recent_skills,
        'most_experienced_skills': most_experienced_skills,
        'most_enjoyable_skills': most_enjoyable_skills,
        'most_proficient_skills': most_proficient_skills,
        'certifications': certifications,
    })



@csrf_exempt
@login_required
def update_user_profile(request, username):

    if request.user.username != username:
        return redirect('index')

    user = get_object_or_404(User, username=username)

    # Add a new skill
    if request.method == 'POST' and 'add_skill' in request.POST:
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = user
            skill.save()
            return redirect('update_user_profile', username=username)

    # Edit a skill
    elif request.method == 'POST' and 'edit_skill' in request.POST:
        skill_id = request.POST.get('skill_id')
        skill = get_object_or_404(Skill, id=skill_id)
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('update_user_profile', username=username)

    # Delete a skill
    elif request.method == 'POST' and 'delete_skill' in request.POST:
        skill_id = request.POST.get('skill_id')
        skill = get_object_or_404(Skill, id=skill_id)
        skill.delete()
        return redirect('update_user_profile', username=username)

    # Form for adding new skills
    form = SkillForm()

    # Get skills
    skills = Skill.objects.filter(user=user)

    return render(request, 'profile2.html', {
        'user': user,
        'skills': skills,
        'form': form,
    })