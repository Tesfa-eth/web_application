from django.contrib import admin
from .models import Post, Universities
# Register your models here.

# add the model I just imported to the adminstrative panel
admin.site.register(Post)
admin.site.register(Universities)