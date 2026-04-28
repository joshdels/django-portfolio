from rest_framework.routers import DefaultRouter
from .views import CaseStudyViewSet

router = DefaultRouter()

router.register(r"", CaseStudyViewSet, basename="case-study")

urlpatterns = router.urls
