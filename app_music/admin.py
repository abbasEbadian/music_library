from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Artist)
admin.site.register(models.Album)
admin.site.register(models.Track)
admin.site.register(models.Tag)
admin.site.register(models.UserProfile)
