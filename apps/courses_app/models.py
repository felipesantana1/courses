# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CoursesManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'Course name must be more than 5 characters'
        if len(postData['desc']) < 15:
            errors['desc'] = 'Description must be more than 15 characters'
        return errors

class Courses(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CoursesManager()

class Desc(models.Model):
    description = models.TextField(null=True)
    course = models.OneToOneField(Courses, related_name='desc', on_delete=models.CASCADE)