from __future__ import unicode_literals
from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    website = models.URLField()

    def __str__(self):          # to return string representation, MUST RETURN ONLY STRING, ELSE TypeError
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return u'%s %s' %(self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __str__(self):
        return self.title