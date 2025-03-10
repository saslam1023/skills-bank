# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView
from .models import Skill, Category, Context, Category, Profile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2


    def save(self, commit=True):
            user = super().save(commit=False)
            if commit:
                user.save()
                Profile.objects.create(user=user)  
            return user


class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'password_reset_email.html'  
    subject_template_name = 'password_reset_subject.txt'  
    success_url = reverse_lazy('password_reset_done')
    html_email_template_name = 'password_reset_email.html' 

    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=None):
        subject = render_to_string(subject_template_name, context).strip()
        html_email = render_to_string(html_email_template_name, context)

        self.get_connection().send_mail(
            subject,
            '',  
            from_email,
            [to_email],
            html_message=html_email,
        )


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('password_reset_complete')  

class CustomPasswordResetDoneView(PasswordResetDoneView):
    success_url = reverse_lazy('password_reset_done')  
    


#CGPT
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency', 'experience', 'enjoyment', 'context', 'certification', 'category']
    
    # Optional custom field for proficiency, experience, and enjoyment
    proficiency = forms.ChoiceField(choices=Skill._meta.get_field('proficiency').choices)
    experience = forms.ChoiceField(choices=Skill._meta.get_field('experience').choices)
    enjoyment = forms.ChoiceField(choices=Skill._meta.get_field('enjoyment').choices)
    
    # Checkbox fields for context and category
    context = forms.ModelMultipleChoiceField(
        queryset=Context.objects.all(), 
        widget=forms.CheckboxSelectMultiple(attrs={"class": "context-options"}), 
        required=False)

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(), 
        widget=forms.CheckboxSelectMultiple(attrs={"class": "category-options"}),  
        required=False)


class SimpleSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']




class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-textarea'}))
