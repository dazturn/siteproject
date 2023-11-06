from django.shortcuts import render

from django.http import HttpResponse
from .models import Profile, SocialMediaLink, Project, Skill, Education, Experience, Image

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ProfileSerializer, SocialSerializer, ProjectSerializer, SkillSerializer, EducationSerializer, ExperienceSerializer, ImageSerializer

# Includes Profile, SocialMediaLink, Image
# Soon, I am hoping to add redirection links to the other pages.
class IndexAPIView(APIView):
    def get(self, request):
        logger.debug('Debug message for index view.')
        p_data = Profile.objects.all()
        p_serializer = ProfileSerializer(p_data, many=True)

        so_data = SocialMediaLink.objects.all()
        so_serializer = SocialSerializer(so_data, many=True)

        i_data = Image.objects.all()
        i_serializer = ImageSerializer(i_data, many=True)

        index_data = {
            'p_data': p_serializer.data,
            'so_data': so_serializer.data,
            'i_data': i_serializer.data,
        }
        return Response(index_data, status.HTTP_200_OK)

# Includes Skill, Education and Experience models
class ProfAPIView(APIView):
    def get(self, request):
        s_data = Skill.objects.all()
        s_serializer = SkillSerializer(s_data, many=True)

        ed_data = Education.objects.all()
        ed_serializer = EducationSerializer(ed_data, many=True)

        ex_data = Experience.objects.all()
        ex_serializer = ExperienceSerializer(ex_data, many=True)

        chosen_data = {
            's_data': s_serializer.data,
            'ed_data': ed_serializer.data,
            'ex_data': ex_serializer.data,
        }
        return Response(chosen_data, status.HTTP_200_OK)
    
# Includes Project Model
class ProjectAPIView(APIView):
    def get(self, request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)