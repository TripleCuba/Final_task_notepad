from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    total_notes = models.IntegerField(default=0)


class Category(models.Model):
    category_title = models.CharField(max_length=100)
    category_image = models.ImageField(null=True, blank=True, default='default.jpg')
    description = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.category_title


class Note(models.Model):
    title = models.CharField(max_length=100)
    note_text = models.CharField(max_length=450)
    note_image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='uncategorized')
