from django.contrib import admin

from .models import (
    Embroidery,
    Book,
    Order,
    EmbroideryImage,
    BookImage,
)

admin.site.register(Embroidery)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(EmbroideryImage)
admin.site.register(BookImage)
