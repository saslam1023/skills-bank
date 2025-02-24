from django.core.management.base import BaseCommand
from app.models import Category, Context

class Command(BaseCommand):
    help = "Insert predefined categories and contexts into the database"

    def handle(self, *args, **kwargs):
        categories = sorted([
            "Artificial Intelligence",
            "Art & Illustration",
            "Business & Project Management",
            "Business Analysis",
            "Cloud & DevOps",
            "Communication & Soft Skills",
            "Cooking & Culinary Arts",
            "Data Science & AI",
            "Design & Creative Skills",
            "DIY & Maker Activities",
            "Education & Training",
            "Electronics & Hardware Hacking",
            "Finance & Accounting",
            "Freelance Work",
            "Game Development",
            "Handicrafts & DIY",
            "Hobby & Experimentation",
            "Human Resources (HR)",
            "Language Learning & Translation",
            "Marketing & SEO",
            "Music & Audio Production",
            "Personal Projects",
            "Photography & Videography",
            "Professional Work",
            "Programming",
            "Public Speaking & Event Hosting",
            "Sales & Customer Service",
            "Sports & Fitness",
            "Streaming & Content Creation",
            "Volunteering",
            "Web Development",
            "Writing & Content Creation"
        ])

        contexts = sorted([
            "Professional Work",
            "Personal Project",
            "Volunteering",
            "Research",
            "Freelance Work",
            "Educational Assignment"
        ])

        # Insert categories into the database
        for category in categories:
            Category.objects.get_or_create(name=category)

        # Insert contexts into the database
        for context in contexts:
            Context.objects.get_or_create(name=context)

        self.stdout.write(self.style.SUCCESS("Successfully added categories and contexts"))
