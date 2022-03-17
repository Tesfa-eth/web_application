from ast import mod
from django.db import models

# Create your models here.

# After adding the models
# python manage.py makemigrations     : applys the model changes
# 
class Post(models.Model):
    postcontent = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()
    postNum = models.IntegerField()
    upvoteCount = models.IntegerField()
    downvoteCount = models.IntegerField()
    ratedBodyID = models.IntegerField()
    rate_stars = models.IntegerField()

    def __str__(self):
        return self.postcontent