from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class student(models.Model):
    mentor = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.TextField()
    school_level = models.IntegerField()
    total_classes = models.IntegerField(default=0)
    attended_classes = models.IntegerField(default=0)
    discussion_score = models.IntegerField(default=0)
    prediction_score = models.IntegerField(default=2)

