from django.db import models

# Come back and add thorough comments
class Profile(models.Model):
    owner_name = models.CharField(max_length = 20)
    contact_info = models.CharField(max_length = 75)
    owner_bio = models.CharField(max_length = 200)

    def __str__(self):
        return self.owner_name
    
    def __str__(self):
        return self.contact_info
    
    def __str__(self):
        return self.owner_bio
    
class SocialMediaLink(models.Model):
   LINKEDIN = 'LinkedIn'
   GITHUB = 'GitHub'

   PLATFORM_CHOICES = [
        ('LinkedIn', 'LinkedIn'),
        ('GitHub', 'GitHub'),
    ]
   
   platform = models.CharField(max_length = 20, choices = PLATFORM_CHOICES)
   url = models.URLField()
   icon = models.ImageField(upload_to = 'social_media_icons/', null = True, blank = True)

   def __str__(self):
       return self.platform
   
   def __str__(self):
        return self.url
   
   def __str__(self):
        return self.icon
   
class Project(models.Model):
    pj_title = models.CharField(max_length = 20)
    pj_description = models.CharField(max_length = 100)
    date_completed = models.DateField()

    def __str__(self):
        return self.pj_title
    
    def __str__(self):
        return self.pj_description
    
    def __str__(self):
        return self.date_completed

class Skill(models.Model):
    skill_name = models.CharField(max_length = 20)
    skill_level = models.CharField(max_length = 15)

    def __str__(self):
        return self.skill_name
    
    def __str__(self):
        return self.skill_level

class Education(models.Model):
    institution = models.CharField(max_length = 20)
    degree = models.CharField(max_length = 20)
    major_minor = models.CharField(max_length = 50)
    grad_date = models.DateField()

    def __str__(self):
        return self.institution
    
    def __str__(self):
        return self.degree
    
    def __str__(self):
        return self.major_minor
    
    def __str__(self):
        return self.grad_date

class Experience(models.Model):
    company = models.CharField(max_length = 50)
    job_title = models.CharField(max_length = 50)
    job_description = models.CharField(max_length = 100)
    duration = models.CharField(max_length = 35)

    def __str__(self):
        return self.company
    
    def __str__(self):
        return self.job_title
    
    def __str__(self):
        return self.job_description
    
    def __str__(self):
        return self.duration

class Image(models.Model):
    image_title = models.CharField(max_length = 15)
    image = models.ImageField(upload_to = 'images/', null = True, blank = True)

    def __str__(self):
        return self.image_title
    
    def __str__(self):
        return self.image
