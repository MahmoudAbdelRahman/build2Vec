from django.db import models
from django.contrib.auth.models import User
import uuid
import os
from django.utils.deconstruct import deconstructible


from django.conf import settings
from google.cloud import storage
from django.core.validators import EmailValidator


class Project(models.Model):
    project_api_key = models.CharField(max_length = 300)
    project_name = models.CharField(max_length = 300)
    email = models.EmailField()

    ifc_file = models.FileField(upload_to = "project")
    # users = models.ManyToManyField(User, related_name="Buildingusers")

    def __str__(self):
        return self.project_name


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid.uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

path_and_rename = PathAndRename("projects")
