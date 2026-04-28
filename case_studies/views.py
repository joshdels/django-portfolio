from rest_framework import viewsets
from .models import CaseStudy, CaseStudyBlock
from .serializers import (
    CaseStudySerializer,
    CaseStudyListSerializer,
    CaseStudyBlockSerializer,
)


class CaseStudyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CaseStudy.objects.all().order_by("-created_at")

    def get_serializer_class(self):
        if self.action == "list":
            return CaseStudyListSerializer
        return CaseStudySerializer


class CaseStudyBlockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CaseStudyBlock.objects.all().order_by("order")
    serializer_class = CaseStudyBlockSerializer
