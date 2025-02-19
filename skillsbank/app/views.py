from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomPasswordResetView, CustomUserCreationForm, SkillForm
from .models import Skill, Category
import json




""" Home (User Logged in)"""
@login_required
def home(request):
    return render(request, 'home.html')


""" Index (Public)"""
def index(request):
    return render(request, 'index.html')

""" Terms (Public)"""
def terms(request):
    return render(request, 'add-skill.html')

""" Privacy (Public)"""
def privacy(request):
    return render(request, 'privacy-policy.html')

""" About (Public)"""
def about(request):
    return render(request, 'about.html')

""" Contact (Public)"""
def contact(request):
    return render(request, 'contact.html')

""" CS50 Test page (Public)"""
def cs50(request):
    return render(request, 'cs50.html')

"""  (Public)"""
#@csrf_exempt
#@login_required
def add_skill(request):
    return render(request, 'add-skill.html')


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

"""  Forgot Password (Public)"""
def forgot_password_view(request):
    return CustomPasswordResetView.as_view(template_name='forgot_password.html')(request)

"""  Password Reset (Public)"""
def password_reset_view(request):
    return CustomPasswordResetView.as_view(template_name='password_reset_request.html')(request)


""" Skills """
# Main Site Content

""" User Skills """
def user_skills(request):
    skills = Skill.objects.filter(user=request.user)
    return render(request, 'skills-list.html', {'skills': skills})


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


""" Add user skills 
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            try:
                skill = form.save(commit=False)
                skill.user = request.user  
                skill.save()  
                messages.success(request, "Skill added successfully!")
                return redirect('user_skills')  
            except Exception as e:
                print(f"Error: {e}")
                return render(request, 'add-skill.html', {'form': form, 'error': 'There was an error adding the skill. Please try again.'}) 
        else:
                return render(request, 'add-skill.html', {'form': form, 'error': 'Invalid form submission. Please correct the errors.'})

    else:
        form = SkillForm()
    
    return render(request, 'add-skill.html', {'form': form})
    """
"""
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            try:
                # Save the form but don't commit yet
                skill = form.save(commit=False)
                skill.user = request.user  # Assign the current user

                # Get multiple checkbox values (context and category) and join them into strings
                context_values = request.POST.getlist('context')
                category_values = request.POST.getlist('category')

                # Join the list of selected values into comma-separated strings
                skill.context = ", ".join(context_values)
                skill.category = ", ".join(category_values)

                # Save the skill instance
                skill.save()

                # Success message and redirection
                messages.success(request, 'Skill added to Skills Bank. View in <a href="{% url "another_view" %}">Skills Bank</a>')
                return redirect('add_skill')
            except Exception as e:
                # Log the error for debugging
                print(f"Error: {e}")
                messages.error(request, "Error adding skill. Try again.")

                return render(request, 'add-skill.html', {'form': form, 'error': 'There was an error adding the skill. Please try again.'})
        else:
            # Print form errors for debugging
            print(form.errors)
            return render(request, 'add-skill.html', {'form': form, 'error': 'Invalid form submission. Please correct the errors.'})
    else:
        form = SkillForm()
    
    return render(request, 'add-skill.html', {'form': form})
"""
"""
@login_required
def add_skill(request):
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            try:
                skill = form.save(commit=False)
                skill.user = request.user

                print("Form Data:", form.cleaned_data)
                print("Context Values:", context_values)


                context_values = request.POST.getlist('context')
                skill.context = context_values

                selected_category_names = request.POST.getlist('category')
                selected_categories = Category.objects.filter(name__in=selected_category_names)
                
                print("Selected Category Names:", selected_category_names)

                skill.category.set(selected_categories)
                print("Skill Saved:", skill)

                skill.save()

                messages.success(request, 'Skill added successfully.')
                return redirect("add_skill")

            except Exception as e:
                print(f"Error: {e}")
                messages.error(request, "Error adding skill. Try again.")
                return render(request, "add-skill.html", {"form": form})

        else:
            print(form.errors)
            messages.error(request, "Invalid form submission. Please correct the errors.")

    else:
        form = SkillForm()

    return render(request, "add-skill.html", {"form": form})
"""

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
