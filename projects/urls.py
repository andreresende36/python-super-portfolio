from django.urls import path
from .views import ProfileListCreateView, ProfileRetrieveUpdateDestroyView

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
]
