from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProfileListCreateView,
    ProfileRetrieveUpdateDestroyView,
    ProjectListCreateView,
    ProjectRetrieveUpdateDestroyView,
    CertificateViewSet,
    CertifyingInstitutionViewSet,
)

router = DefaultRouter()
router.register(r"certifying-institutions", CertifyingInstitutionViewSet)
router.register(r"certificates", CertificateViewSet)

urlpatterns = [
    path(
        "profiles/",
        ProfileListCreateView.as_view(),
        name="profile-list-create",
    ),
    path(
        "profiles/<int:pk>/",
        ProfileRetrieveUpdateDestroyView.as_view(),
        name="profile-retrieve-update-destroy",
    ),
    path(
        "projects/",
        ProjectListCreateView.as_view(),
        name="project-list-create",
    ),
    path(
        "projects/<int:pk>/",
        ProjectRetrieveUpdateDestroyView.as_view(),
        name="project-retrieve-update-destroy",
    ),
    path("", include(router.urls)),
    path(
        "profiles/<int:pk>/",
        ProfileRetrieveUpdateDestroyView.as_view(),
        name="profile-detail",
    ),
]
