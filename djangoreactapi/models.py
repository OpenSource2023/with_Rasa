from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class UserProfile(AbstractUser):
    gender = models.CharField(max_length=10, null=True, blank=False)
    birth = models.DateField(null=True, blank=False)
    phone = models.CharField(max_length=15, null=True, blank=False)
    groups = models.ManyToManyField(Group, related_name='user_profiles_groups')
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='user_profiles_permissions'
    )

    # 유니크 제약 추가
    username = models.CharField(max_length=255, unique=True)

class UserGroup(models.Model):
    user = models.OneToOneField(UserProfile, related_name='profile', on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, related_name='user_groups')
