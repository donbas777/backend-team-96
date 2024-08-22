from django.contrib import admin

from .models import (
    Embroidery,
    Book,
    Order,
)

admin.site.register(Embroidery)
admin.site.register(Book)
admin.site.register(Order)
