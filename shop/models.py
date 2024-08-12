import os
import uuid

from django.db import models
from django.utils.text import slugify


def vyshyvanka_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/vyshyvanka/", filename)


def books_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/books/", filename)


class Vyshyvanka(models.Model):
    class CategoryChoice(models.TextChoices):
        MALE = "MALE"
        FEMALE = "FEMALE"
        BOY = "BOY"
        GIRL = "GIRL"

    class SizeChoice(models.TextChoices):
        XS = "XS"
        S = "S"
        M = "M"
        L = "L"
        XL = "XL"
        XXL = "XXL"

    name = models.CharField(max_length=255)
    category = models.CharField(choices=CategoryChoice)
    size = models.CharField(choices=SizeChoice)
    price = models.IntegerField()
    image = models.ImageField(null=True, upload_to=vyshyvanka_image_file_path)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    pages = models.IntegerField()
    genre = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(null=True, upload_to=books_image_file_path)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
