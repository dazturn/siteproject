from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, SocialMediaLink, Project, Skill, Education, Experience, Image
from .serializers import ProfileSerializer, SMLSerializer, ProjectSerializer, SkillSerializer, EducationSerializer, ExperienceSerializer, ImageSerializer

class ProfileListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class SocialMediaLinkListView(ListAPIView):
    queryset = SocialMediaLink.objects.all()
    serializer_class = SMLSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class SkillListView(ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class EducationListView(ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class ExperienceListView(ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class ImageListView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
