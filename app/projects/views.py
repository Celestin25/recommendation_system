from django.conf import settings
from rest_framework import generics, status
from django.core.mail import send_mail
from projects.models import (
    Project,
    ProjectImageAlbum,
    ProjectInvitation
)
from projects.serializers import (
    ProjectSerializer,
    PhotoSerializer,
    ProjectInvitationSerializer,
    ProjectInvitationAcceptSerializer
)
from projects.permissions import IsInvitee
from utils.permissions import (
    IsOwnerOrReadOnly,
    IsAuthUserOrReadOnly
)
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.sites.shortcuts import get_current_site


class ProjectsListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthUserOrReadOnly]


class ProjectDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ProjectInvitationCreateView(generics.CreateAPIView):
    queryset = ProjectInvitation.objects.all()
    serializer_class = ProjectInvitationSerializer

    def perform_create(self, serializer):
        invitation = serializer.save(inviter=self.request.user)
        self.send_invitation_email(invitation)

    def send_invitation_email(self, invitation):
        domain = get_current_site(self.request).domain
        invite_link = f"{domain}/invite/{invitation.token}"
        send_mail(
            'You are invited to join a project',
            f'Click the link to join: {invite_link}',
            settings.DEFAULT_FROM_EMAIL,
            [invitation.invitee_email],
            fail_silently=False,
        )


class ProjectInvitationAcceptView(generics.GenericAPIView):
    serializer_class = ProjectInvitationAcceptSerializer
    permission_classes = [IsInvitee]

    def get(self, request, token):
        invitation = get_object_or_404(ProjectInvitation, token=token)
        if invitation.accepted:
            return Response({'detail': 'Invitation already accepted'}, status=status.HTTP_400_BAD_REQUEST)

        invitation.project.collaborators.add(request.user)
        invitation.accepted = True
        invitation.save()
        return Response({'detail': 'Invitation accepted'}, status=status.HTTP_200_OK)
