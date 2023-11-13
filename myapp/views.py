from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Profile, SocialMediaLink, Project, Skill, Education, Experience, Image
from .serializers import ProfileSerializer, SMLSerializer, ImageSerializer, ProjectSerializer, SkillSerializer, EducationSerializer, ExperienceSerializer

# Profile, Social Media Link and Image views.
class IndexAPIView(ListAPIView):   
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = None

    def get(self, request, format=None):
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

        return Response(data)

# Skill, Education and Experience views.
class ProfAPIView(ListAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = None

    def get(self, request, format=None):
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

        return Response(data)

# The only view for this URL case so far.
class ProjectAPIView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()