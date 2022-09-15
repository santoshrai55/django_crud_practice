from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='crud_app/images/')
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title + ' by '+str(self.author.first_name)
