from django.urls import path
from .views import (
    ProfileListCreateView,
    ProfileRetrieveUpdateDestroyView,
    ProjectListCreateView,
    ProjectRetrieveUpdateDestroyView,
)

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
]
