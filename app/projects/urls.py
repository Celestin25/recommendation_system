from django.urls import path
from projects.views import (
    ProjectsListView,
    ProjectDetailsView,
    ProjectInvitationCreateView,
    ProjectInvitationAcceptView
)


urlpatterns = [
    path('', ProjectsListView.as_view(), name='projects-list'),
    path('<int:pk>/', ProjectDetailsView.as_view(), name='project-details'),
    path(
        'invitations/',
        ProjectInvitationCreateView.as_view(),
        name='project_invitations'
    ),
    path(
        'invitations/accept/<uuid:token>/',
        ProjectInvitationAcceptView.as_view(),
        name='accept_project_invitation'
    ),
]
