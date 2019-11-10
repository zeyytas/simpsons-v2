
from django.db import models
import os
from django.db.models.fields.files import ImageField


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Client(models.Model):
    company_name = models.CharField(max_length=25, null=False)
    country = models.CharField(max_length=25, null=False)

    def __str__(self):
        return self.company_name


class Projects(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=50, null=False)
    starting_date = models.DateTimeField(null=True, blank=True)
    deadline = models.DateField(null=False, blank=True)
    about = models.TextField(max_length=1500, null=True)

    def __str__(self):
        return self.name


class Characters(models.Model):
    image = ImageField(upload_to=get_image_path, blank=True, null=True)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=25)
    birthday = models.DateField(null=True)
    phone_number = models.CharField(max_length=12, null=True, )
    mail = models.EmailField(null=True)
    info = models.TextField(null=True, max_length=600)
    likes = models.TextField(null=True, max_length=600)

    projects = models.ForeignKey(Projects, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def searchable(self):
        return self.name + self.position + self.info


class Company(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    about = models.CharField(max_length=1500, null=True, blank=True)
    logo = ImageField(upload_to=get_image_path, blank=True, null=True)


    def __str__(self):
        return self.name
