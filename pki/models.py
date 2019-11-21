from django.db import models

# Create your models here.
#
#
class UserInfo(models.Model):
    userID = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    pubkeyInfo = models.CharField(max_length=256)


