from django.contrib import admin
from .models import Skill, Project, AIAnalysis, Portfolio, Category, Context

admin.site.register(Category)
admin.site.register(Context)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(AIAnalysis)
admin.site.register(Portfolio)
