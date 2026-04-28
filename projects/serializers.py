from rest_framework import serializers
from .models import Project, ProjectBlock


class ProjectBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectBlock
        fields = "__all__"


class ProjectListSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    blocks = ProjectBlockSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
