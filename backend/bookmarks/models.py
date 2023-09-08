from django.db import models
from common.models import BaseModel
from accounts.models import User
# Create your models here.

class Bookmark(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user")
    title = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.TextField(null=True, blank=True)
    site_name = models.CharField(max_length=250, null=True, blank=True)
    collaborators = models.ManyToManyField(User, blank=True)

    def __str__(self) -> str:
        return str(self.title)
