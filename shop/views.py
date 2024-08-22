from rest_framework import mixins, status, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import Embroidery, Book, Order
from .serializers import (
    EmbroiderySerializer,
    EmbroideryImageSerializer,
    BookSerializer,
    BookListSerializer,
    BookImageSerializer,
    OrderSerializer
)


class EmbroideryViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    queryset = Embroidery.objects.all()
    serializer_class = EmbroiderySerializer
    permission_classes = ()

    def get_queryset(self):
        """Retrieve the movies with filters"""
        name = self.request.query_params.get("name")
        category = self.request.query_params.get("category")
        sizes = self.request.query_params.get("sizes")
        price = self.request.query_params.get("price")

        queryset = self.queryset

        if name:
            queryset = queryset.filter(name__icontains=name)

        if category:
            queryset = queryset.filter(category__icontains=category)

        if sizes:
            queryset = queryset.filter(sizes__icontains=sizes)

        if price:
            queryset = queryset.filter(price=price)

        return queryset

    def get_serializer_class(self):

        if self.action == "upload_image":
            return EmbroideryImageSerializer

        return EmbroiderySerializer

    @action(
        methods=["POST"],
        detail=True,
        url_path="upload-image",
        permission_classes=[IsAdminUser],
    )
    def upload_image(self, request, pk=None):
        embroidery = self.get_object()
        serializer = self.get_serializer(embroidery, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class BookViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = ()

    def get_queryset(self):
        """Retrieve the movies with filters"""
        title = self.request.query_params.get("title")
        description = self.request.query_params.get("description")
        genre = self.request.query_params.get("genre")
        price = self.request.query_params.get("price")

        queryset = self.queryset

        if title:
            queryset = queryset.filter(title__icontains=title)

        if description:
            queryset = queryset.filter(description__icontains=description)

        if genre:
            queryset = queryset.filter(genre__icontains=genre)

        if price:
            queryset = queryset.filter(price=price)

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return BookListSerializer

        if self.action == "upload_image":
            return BookImageSerializer

        return BookSerializer

    @action(
        methods=["POST"],
        detail=True,
        url_path="upload-image",
        permission_classes=[IsAdminUser],
    )
    def upload_image(self, request, pk=None):
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class OrderPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100


class OrderViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = Order.objects.prefetch_related(
        "embroideries", "books"
    )
    serializer_class = OrderSerializer
    pagination_class = OrderPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
