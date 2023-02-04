from django.db import models
from account.models import User
from django.utils import timezone
# from datetime import datetime

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    desctiption=models.TextField()
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    created=models.DateTimeField(auto_now_add=True )
    updated=models.DateTimeField(auto_now=True)
    publish=models.DateTimeField(default=timezone.now)