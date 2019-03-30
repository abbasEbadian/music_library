from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=30, default='Various Artists')

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,default='Unknown Album')
    short_description = models.CharField(max_length=300)
    long_description = models.TextField(blank=True)
    rate = models.FloatField(null=True,default=0,)
    likes = models.PositiveSmallIntegerField(default=0,null=True)
    release_date = models.DateField()
    avatar = models.ImageField(upload_to='albums/covers/')
    tags = models.ManyToManyField(Tag,related_name='tags')
    def __str__(self):
        return self.title


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    music_file = models.FileField(upload_to='albums/tracks/')

    def __str__(self):
        return self.title
