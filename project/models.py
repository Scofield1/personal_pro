from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Skill(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    progress = models.IntegerField(default=80, blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    project_url = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(default='', upload_to='portfolio')
    created = models.DateTimeField(auto_now_add=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='portfolio/images/')

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default='', upload_to='testimonial')

    def __str__(self):
        return self.name

