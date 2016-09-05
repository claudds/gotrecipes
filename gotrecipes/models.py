from django.db import models
from PIL import Image

# Create your models here.
class Recipe(models.Model):
  title=models.CharField(max_length=200)
  ingredients=models.TextField()
  directions=models.TextField()
  image = models.ImageField(upload_to='recipe_images', default='recipe_images/default.png')
  
  def __str__(self):
    return self.title