import uuid
from django.db import models
from inventory.models import Equipment
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model


User = get_user_model()


class Project(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = CloudinaryField(
        'image', folder='fabla/projects/thumbnails', null=True, blank=True
    )
    tagline = models.CharField(max_length=255)
    equipments = models.ManyToManyField(Equipment, related_name='projects', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_owned')
    collaborators = models.ManyToManyField(
        User, related_name='projects_as_collaborator', blank=True)
    about = models.TextField()
    demo_video_url = models.URLField(blank=True, null=True)
    other_links = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.owner in self.collaborators.all():
            self.collaborators.remove(self.owner)
        super(Project, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']


class ProjectImageAlbum(models.Model):
    image = CloudinaryField(
        'image', folder='fablab/projects/images', null=True, blank=True
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='images'
    )


class ProjectLike(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['project', 'user']
        ordering = ['-created_at']


class ProjectComment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class ProjectInvitation(models.Model):
    inviter = models.ForeignKey(
        User, related_name='invitations_sent', on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, related_name='invitations', on_delete=models.CASCADE)
    invitee_email = models.EmailField()
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)


    @property
    def invitee(self):
        return User.objects.filter(email=self.invitee_email).first()