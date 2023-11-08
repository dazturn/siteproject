from django.contrib import admin

from django.contrib import admin
from .models import Profile, SocialMediaLink, Project, Skill, Education, Experience, Image

# Registered models
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'contact_info', 'owner_bio')

@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pj_title', 'pj_description', 'date_completed')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'skill_level')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'major_minor', 'grad_date')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'job_title', 'job_description', 'duration')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_title', 'image')