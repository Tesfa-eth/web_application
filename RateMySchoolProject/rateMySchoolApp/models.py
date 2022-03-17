from ast import mod
from enum import auto
from django.db import models
from django.utils import timezone # get time zone
# Create your models here.
# After adding the models
# python manage.py makemigrations     : applys the model changes
# python manage.py migrate       : now it migrates all the models including the one I just created
# created super user
# username = Admin, password = Muler**********
class Post(models.Model):
    postcontent = models.CharField(max_length=200)
    # changed the the zone in settings.py from UTC to EST
    date_created = models.DateTimeField(default=timezone.now())
    # user_id = models.IntegerField()
    # postNum = models.IntegerField()
    # upvoteCount = models.IntegerField()
    # downvoteCount = models.IntegerField()
    # ratedBodyID = models.IntegerField()
    # rate_stars = models.IntegerField()

    def __str__(self):
        return self.postcontent# what it shows us on the admin panel.