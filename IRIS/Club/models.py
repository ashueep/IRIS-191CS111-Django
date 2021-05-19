# from typing_extensions import Required
from django.db import models
# from User.models import User
from django.utils import timezone
# Create your models here.
class Club(models.Model):
    name        = models.CharField(verbose_name = 'Club Name', max_length = 24)
    convener    = models.ForeignKey("User.User", default = None, on_delete = models.SET_NULL, related_name = 'Convener', null = True, blank = True)
    dateCreated = models.DateField(default = timezone.now)

    def __str__(self):
        return self.name

    