from django.db import models


# Create your models here.
class Elements(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


# git remote add origin git@github.com:AlexTsikhun/django-simple-show-db.git
