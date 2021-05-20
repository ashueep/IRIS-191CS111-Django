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

class Items(models.Model):
    name     = models.CharField(verbose_name = 'Item Name', max_length = 200, unique = False)
    quantity = models.IntegerField(verbose_name = 'Quantity')
    club     = models.ForeignKey(Club, on_delete = models.CASCADE, related_name = 'item_club')

    def __str__(self):
        return self.name

class RequestStatus(models.Model):
    description = models.CharField(max_length=27)
    def __str__(self):
        return self.description

class ItemRequest(models.Model):
    memberID    = models.ForeignKey("User.User", on_delete = models.CASCADE)
    itemID      = models.ForeignKey(Items, on_delete = models.CASCADE)
    createdOn   = models.DateField(default=timezone.now)
    requested   = models.IntegerField(verbose_name="Number of requested items ")
    club        = models.ForeignKey(Club, on_delete = models.CASCADE)
    status      = models.ForeignKey(RequestStatus, on_delete = models.CASCADE)
    def __str__(self):
        return self.memberID.userName + "-" + self.itemID.name