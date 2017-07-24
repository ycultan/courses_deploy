from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 11:
            errors['name'] = "Course name must be at least 10 characters"
        if len(postData['desc']) < 16:
            errors['desc'] = "Description must be at least 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()