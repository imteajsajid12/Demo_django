from django.db import models

# Create your models here.

#todoapp models

class Data(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    descriptions = models.TextField(blank=True)
    
    
    
