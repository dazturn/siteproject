from rest_framework import serializers
# Individual serializers
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class SMLSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

# Grouped serializers
class IndexSerializer(serializers.Serializer):
    profile = ProfileSerializer(many=True)
    sml = SMLSerializer(many=True)
    images = ImageSerializer(many=True)

class ProfSerializer(serializers.Serializer):
    skills = SkillSerializer(many=True)
    education = EducationSerializer(many=True)
    experience = ExperienceSerializer(many=True)