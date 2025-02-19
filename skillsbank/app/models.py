from django.db import models
from django.contrib.auth.models import User

# Skill
class Skill(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=255)
    proficiency = models.PositiveIntegerField(choices=[
        (2, "Beginner"),
        (3, "Intermediate"),
        (4, "Advanced"),
        (5, "Expert"),
        (6, "Master"),
    ])
    experience = models.PositiveIntegerField(choices=[
        (1, "Limited"),
        (2, "Basic"),
        (3, "Moderate"),
        (4, "Extensive"),
        (5, "Vast"),
    ])
    enjoyment = models.PositiveIntegerField(choices=[
        (1, "Dislike"),
        (2, "Neutral"),
        (3, "Moderate"),
        (4, "Strong"),
        (5, "Passionate"),
    ])
    context = models.ManyToManyField('Context', blank=True)
    certification = models.CharField(max_length=255, blank=True, null=True)
    category = models.ManyToManyField('Category', blank=True)

    def __str__(self):
        return self.name


# Skill: Context
class Context(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Skill: Category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 2. Project Model
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    situation = models.TextField(help_text="Describe the context or problem you faced.")
    task = models.TextField(help_text="Explain what your responsibility was in this situation.")
    action = models.TextField(help_text="Detail the steps you took to address the task.")
    result = models.TextField(help_text="Describe the outcome of your actions.")
    skills_used = models.ManyToManyField('Skill')
    key_learnings = models.TextField(blank=True, help_text="Summarize what you learned from this experience.")
    feedback = models.TextField(blank=True, help_text="Include any feedback received from peers or mentors.")
    rating = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        blank=True, null=True,
        help_text="Rate the project experience from 1 (low) to 5 (high)."
    )
    
    completed_on = models.DateField()
    
    def __str__(self):
        return self.title

# 3. AI Analysis Model
class AIAnalysis(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    strongest_skill = models.CharField(max_length=100)
    most_experienced_skill = models.CharField(max_length=100)
    most_enjoyed_skill = models.CharField(max_length=100)
    analysis_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AI Analysis for {self.user.username}"

# 4. Portfolio Model
class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return f"Portfolio for {self.user.username}"
