from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Profile, SocialMediaLink, Project, Skill, Education, Experience, Image
from .serializers import IndexSerializer, ProfSerializer, ProjectSerializer

# Profile, Social Media Link and Image views.
class IndexAPIView(ModelViewSet):
    serializer_class = IndexSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        profiles = Profile.objects.all()
        sml = SocialMediaLink.objects.all()
        images = Image.objects.all()
        return {'profiles': profiles, 'sml': sml, 'images': images}

# Skill, Education and Experience views.
class ProfAPIView(ModelViewSet):
    serializer_class = ProfSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        skills = Skill.objects.all()
        education = Education.objects.all()
        experience = Experience.objects.all()
        return {'skills': skills, 'education': education, 'experience': experience}

# The only view for this URL case so far.
class ProjectAPIView(ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Project.objects.all()