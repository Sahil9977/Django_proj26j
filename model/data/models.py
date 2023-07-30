from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class Note(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()
    slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)

# Create your models here.
