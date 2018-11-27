from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    slug = models.SlugField('Slug', unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.TextField()
    #members = models.ManyToManyField(User, through='Member', related_name='members')

    def __str__(self):
        return self.name


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.CharField(max_length=50)
    LEVEL_ASSES = (
        ('U', 'User'),
        ('A', 'Admin'),
        ('I', 'Invited')
    )
    level_asses = models.CharField(max_length=50, choices=LEVEL_ASSES)
    id_team = models.CharField(max_length=50)

    def __str__(self):
        return_ = "User " + self.id_user.username + " é " + self.level_asses + " do team " + self.id_team
        return return_

