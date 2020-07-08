from django.db import models

# Create your models here.
#
#
class UserInfo(models.Model):
    userID = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    pubkeyInfo = models.CharField(max_length=256)
    #cyy2020
    #report = models.FileField(db_index=True, upload_to='not_used')


