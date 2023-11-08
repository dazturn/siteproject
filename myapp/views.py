from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, SocialMediaLink, Project, Skill, Education, Experience, Image
from .serializers import ProfileSerializer, SMLSerializer, ProjectSerializer, SkillSerializer, EducationSerializer, ExperienceSerializer, ImageSerializer

class ProfileListView(ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Profile.objects.all()

class SocialMediaLinkListView(ListAPIView):
    serializer_class = SMLSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return SocialMediaLink.objects.all()

class ProjectListView(ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Project.objects.all()

class SkillListView(ListAPIView):
    serializer_class = SkillSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Skill.objects.all()

class EducationListView(ListAPIView):
    serializer_class = EducationSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Education.objects.all()

class ExperienceListView(ListAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Experience.objects.all()

class ImageViewList(ListAPIView):
    serializer_class = ImageSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Image.objects.all()
