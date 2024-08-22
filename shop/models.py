import os
import uuid

from django.db import models
from django.utils.text import slugify
from django.conf import settings
from multiselectfield import MultiSelectField


def embroidery_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.name)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/embroidery/", filename)


def books_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/books/", filename)


class Embroidery(models.Model):
    class CategoryChoice(models.TextChoices):
        MALE = "MALE"
        FEMALE = "FEMALE"
        BOY = "BOY"
        GIRL = "GIRL"

    OPTION_CHOICES = (
        ("XS", "XS"),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
    )

    name = models.CharField(max_length=255)
    category = models.CharField(choices=CategoryChoice, max_length=50)
    sizes = MultiSelectField(choices=OPTION_CHOICES)
    price = models.IntegerField()
    image = models.ImageField(null=True, upload_to=embroidery_image_file_path)

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


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    embroideries = models.ManyToManyField(Embroidery, blank=True)
    books = models.ManyToManyField(Book, blank=True)

    class Meta:
        ordering = ["-created_at"]
