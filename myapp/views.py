from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render
from django.http import HttpResponse

from .models import Profile, SocialMediaLink, Project, Skill, Education, Experience, Image
from .serializers import ProfileSerializer, SMLSerializer, ImageSerializer, ProjectSerializer, SkillSerializer, EducationSerializer, ExperienceSerializer

# Profile, Social Media Link and Image views.
class IndexAPIView(APIView):
    # View queryset creation.
    def get_data(self, request):
        profiles = Profile.objects.all()
        sml = SocialMediaLink.objects.all()
        images = Image.objects.all()

        profile_serializer = ProfileSerializer(profiles, many=True)
        sml_serializer = SMLSerializer(sml, many=True)
        images_serializer = ImageSerializer(images, many=True)

        data = {
            'profiles': profile_serializer.data,
            'sml': sml_serializer.data,
            'images': images_serializer.data
        }

        return Response(data, status.HTTP_200_OK)

# Skill, Education and Experience views.
class ProfAPIView(APIView):
    #View queryset creation.
    def get_data(self, request):
        skills = Skill.objects.all()
        education = Education.objects.all()
        experience = Experience.objects.all()

        skills_serializer = SkillSerializer(skills, many=True)
        education_serializer = EducationSerializer(education, many=True)
        experience_serializer = ExperienceSerializer(experience, many=True)

        data = {
            'skills': skills_serializer.data,
            'education': education_serializer.data,
            'experience': experience_serializer.data
        }

        return Response(data, status.HTTP_200_OK)

# The only view for this URL case so far.
class ProjectAPIView(APIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()