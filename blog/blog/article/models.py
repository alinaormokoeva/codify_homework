from django.db import models
from datetime import datetime

# Create your models here.

def article_directory_path(instance,filename):
    return 'create/{0}/{1}'.format(datetime.today().strftime('%Y-%m-%d'),filename)

class Article(models.Model):
    title = models.CharField(max_length=150)
    short_description =  models.CharField(max_length=300, null=True)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to=article_directory_path, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date  = models.DateTimeField(auto_now=True)