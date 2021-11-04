from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    body = models.TextField(max_length=2000)
    source_code = models.CharField(max_length=1080, null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='tags', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name