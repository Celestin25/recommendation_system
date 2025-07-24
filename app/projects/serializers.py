from rest_framework import serializers
from projects.models import (
    Project,
    ProjectImageAlbum,
    ProjectLike,
    ProjectComment,
    ProjectInvitation
)


class ProjectLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectLike
        fields = ('user',)


class ProjectCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectComment
        fields = ('user', 'content', 'created_at', 'updated_at')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImageAlbum
        fields = ('image',)


class ProjectSerializer(serializers.ModelSerializer):
    images = PhotoSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInvitation
        fields = ['id', 'inviter', 'invitee_email',
                  'token', 'created_at', 'accepted']
        read_only_fields = ['token', 'created_at', 'accepted']


class ProjectInvitationAcceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInvitation
        fields = ['accepted']
        read_only_fields = ['accepted']
