from django.db import models

class Profile(models.Model):
    owner_name = models.CharField(max_length=20)
    contact_info = models.CharField(max_length=75)
    owner_bio = models.CharField(max_length=200)

    def __str__(self):
        return self.owner_name

class SocialMediaLink(models.Model):
    LINKEDIN = 'LinkedIn'
    GITHUB = 'GitHub'

    PLATFORM_CHOICES = [
        ('LinkedIn', 'LinkedIn'),
        ('GitHub', 'GitHub'),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon = models.ImageField(upload_to='social_media_icons/', null=True, blank=True)

    def __str__(self):
        return f"{self.platform} - {self.url}"

class Project(models.Model):
    pj_title = models.CharField(max_length=20)
    pj_description = models.CharField(max_length=100)
    date_completed = models.DateField()

    def __str__(self):
        return self.pj_title

class Skill(models.Model):
    skill_name = models.CharField(max_length=20)
    skill_level = models.CharField(max_length=15)

    def __str__(self):
        return self.skill_name

class Education(models.Model):
    institution = models.CharField(max_length=20)
    degree = models.CharField(max_length=20)
    major_minor = models.CharField(max_length=50)
    grad_date = models.DateField()

    def __str__(self):
        return self.institution

class Experience(models.Model):
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    job_description = models.CharField(max_length=100)
    duration = models.CharField(max_length=35)

    def __str__(self):
        return self.company

class Image(models.Model):
    image_title = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.image_title

