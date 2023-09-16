from rest_framework.views import APIView, status, Response
from .models import Album
from .serializers import AlbumSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView


class AlbumView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @extend_schema(
        operation_id="album_list",
        summary="Lista todos os albums",
        description="Rota para listar todos os albums",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        operation_id="album_create",
        summary="Cria todos os albums",
        description="Rota para criar todos os albums",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
