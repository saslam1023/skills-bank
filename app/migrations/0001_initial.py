# Generated by Django 5.1.6 on 2025-02-19 18:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AIAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strongest_skill', models.CharField(max_length=100)),
                ('most_experienced_skill', models.CharField(max_length=100)),
                ('most_enjoyed_skill', models.CharField(max_length=100)),
                ('analysis_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('proficiency', models.PositiveIntegerField(choices=[(2, 'Beginner'), (3, 'Intermediate'), (4, 'Advanced'), (5, 'Expert'), (6, 'Master')])),
                ('experience', models.PositiveIntegerField(choices=[(1, 'Limited'), (2, 'Basic'), (3, 'Moderate'), (4, 'Extensive'), (5, 'Vast')])),
                ('enjoyment', models.PositiveIntegerField(choices=[(1, 'Dislike'), (2, 'Neutral'), (3, 'Moderate'), (4, 'Strong'), (5, 'Passionate')])),
                ('certification', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.ManyToManyField(blank=True, to='app.category')),
                ('context', models.ManyToManyField(blank=True, to='app.context')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('situation', models.TextField(help_text='Describe the context or problem you faced.')),
                ('task', models.TextField(help_text='Explain what your responsibility was in this situation.')),
                ('action', models.TextField(help_text='Detail the steps you took to address the task.')),
                ('result', models.TextField(help_text='Describe the outcome of your actions.')),
                ('key_learnings', models.TextField(blank=True, help_text='Summarize what you learned from this experience.')),
                ('feedback', models.TextField(blank=True, help_text='Include any feedback received from peers or mentors.')),
                ('rating', models.PositiveIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text='Rate the project experience from 1 (low) to 5 (high).', null=True)),
                ('completed_on', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('skills_used', models.ManyToManyField(to='app.skill')),
            ],
        ),
    ]
