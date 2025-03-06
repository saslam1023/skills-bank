
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetView, CustomPasswordResetConfirmView, SkillForm
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from app.views import error_404  




urlpatterns = [
    path('', views.index, name='index'),
    path('search-skills/', views.search_users_by_skill, name='search_users_by_skill'),

    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('forgot-password/', CustomPasswordResetView.as_view(template_name='forgot_password.html'), name='forgot_password'),
    path('password-reset-request/', CustomPasswordResetView.as_view(template_name='password_reset_request.html'), name='password_reset_request'),
    path('password_reset/', CustomPasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('privacy-policy/', views.privacy, name='privacy'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('terms-of-use/', views.terms, name='terms'),
    path('cs50/', views.cs50, name='cs50'),

    path('add-skill/', views.add_skill, name='add_skill'),
    path('add-quick-skill/', views.add_quick_skill, name='add-quick-skill'),
    path('skill/edit/<int:skill_id>/', views.edit_skill, name='edit_skill'),
    path('skill/delete/<int:skill_id>/', views.delete_skill, name='delete_skill'),
    path('skills/', views.user_skills, name='user_skills'),
    path('skills-account/', views.skill_account, name='skill_account'),


    path('directory/', views.skills_directory, name='skills_directory'), 
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('<str:username>/', views.public_user_profile, name='public_user_profile'),
    path('demo/', views.demo, name='demo'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'app.views.error_404'
