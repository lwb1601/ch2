from django.db import models

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField('TITLE', max_length=50)
    url = models.URLField('URL', unique=True)

    def __str__(self):
        return self.site_name



