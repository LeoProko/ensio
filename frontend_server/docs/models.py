from django.db import models
from django.contrib.auth.models import Group

from factory.models import User

class Document(models.Model):
    title = models.CharField(max_length=200, null=True)
    owner = models.CharField(max_length=50, null=True)
    authors = models.ManyToManyField(User, blank=True)
    groups = models.ManyToManyField(Group, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    markdown_data = models.TextField(null=True)
    html_data = models.TextField(null=True)
    is_link_public = models.BooleanField(default=False)
    is_indexed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.title)
