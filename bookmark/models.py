from django.db import models

# Create your models here.
class BookmarkSet(models.Model):
    list_name = models.CharField('NAME',max_length=50)
    date = models.DateTimeField('DATE',auto_now=True)

    def __str__(self):
        return self.list_name

class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=50)
    url = models.URLField('URL', unique=True)
    list_id = models.ForeignKey(BookmarkSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

