from rest_framework import serializers

from .models import Book, Embroidery, Order


class EmbroiderySerializer(serializers.ModelSerializer):
    class Meta:
        model = Embroidery
        fields = (
            "id",
            "name",
            "category",
            "sizes",
            "price",
            "image",
        )


class EmbroideryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Embroidery
        fields = ("id", "image")


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "description",
            "pages",
            "genre",
            "price",
            "image",
        )


class BookListSerializer(BookSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "genre",
            "price",
            "image",
        )


class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "image")


class OrderSerializer(serializers.ModelSerializer):
    embroideries = EmbroiderySerializer(many=True, read_only=False, allow_empty=False)
    books = BookSerializer(many=True, read_only=False, allow_empty=False)

    class Meta:
        model = Order
        fields = ("id", "embroideries", "books", "created_at")
