from rest_framework import serializers

from .models import (
    Book,
    Embroidery,
    Order,
    EmbroideryImage,
    BookImage,
)


class EmbroideryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmbroideryImage
        fields = ("image",)


class EmbroiderySerializer(serializers.ModelSerializer):
    images = EmbroideryImageSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Embroidery
        fields = (
            "id",
            "name",
            "category",
            "sizes",
            "price",
            "image",
            "images",
        )

    def get_image(self, obj):
        first_image = obj.images.first()
        if first_image:
            return EmbroideryImageSerializer(first_image).data
        return None


class EmbroideryListSerializer(EmbroiderySerializer):
    class Meta:
        model = Embroidery
        fields = (
            "name",
            "sizes",
            "price",
            "image",
        )


class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ("image",)


class BookSerializer(serializers.ModelSerializer):
    images = BookImageSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

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
            "images",
        )

    def get_image(self, obj):
        first_image = obj.images.first()
        if first_image:
            return BookImageSerializer(first_image).data
        return None


class BookListSerializer(BookSerializer):
    class Meta:
        model = Book
        fields = (
            "title",
            "genre",
            "price",
            "image",
        )


class OrderSerializer(serializers.ModelSerializer):
    embroideries = EmbroiderySerializer(many=True, read_only=False, allow_empty=False)
    books = BookSerializer(many=True, read_only=False, allow_empty=False)

    class Meta:
        model = Order
        fields = ("id", "embroideries", "books", "created_at")
