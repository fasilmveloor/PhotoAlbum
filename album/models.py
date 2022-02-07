from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to = 'images/',null = False, blank=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.description
