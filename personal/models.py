# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


@python_2_unicode_compatible
class About(models.Model):
    title = "About"
    AboutInfo = RichTextUploadingField()

    class Meta:
        verbose_name = "من نحن"
        verbose_name_plural = "من نحن"

    def __str__(self):
        return self.title
        #current to do, how do we return multiple attributes?

@python_2_unicode_compatible
class NewsPost(models.Model):
    title = models.CharField(max_length=120)
    body = RichTextUploadingField()
    date = models.DateTimeField('date published')

    class Meta:
        verbose_name = "اخبار"
        verbose_name_plural = "اخبار"

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class CulturePost(models.Model):
    title = models.CharField(max_length=120)
    body = RichTextUploadingField()
    date = models.DateTimeField('date published')

    class Meta:
        verbose_name = "ثقافة"
        verbose_name_plural =  "ثقافة"

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class ArtPost(models.Model):
    title = models.CharField(max_length=120)
    body = RichTextUploadingField()
    date = models.DateTimeField('date published')

    class Meta:
        verbose_name = "فن"
        verbose_name_plural = "فن"

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class MedPost(models.Model):
    title = models.CharField(max_length=120)
    body = RichTextUploadingField()
    date = models.DateTimeField('date published')

    class Meta:
        verbose_name = "طب"
        verbose_name_plural = "طب"

    def __str__(self):
        return self.title
