from rest_framework import viewsets
from .models import Project, ProjectBlock
from .serializers import (
    ProjectSerializer,
    ProjectListSerializer,
    ProjectBlockSerializer,
)


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all().order_by("-created_at")

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        return ProjectSerializer


class ProjectBlockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProjectBlock.objects.all().order_by("order")
    serializer_class = ProjectBlockSerializer
