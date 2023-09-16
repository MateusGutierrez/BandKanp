from rest_framework.views import APIView, Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from drf_spectacular.utils import extend_schema


class UserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        operation_id="user_create",
        summary="Criação de usuário",
        description="Rota para criar usuários da aplicação",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        operation_id="user_retrieve",
        summary="Lista um usuário por id",
        description="Rota para listar informações de um usuário",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(operation_id="user_put", exclude=True)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        operation_id="user_update",
        summary="Atualiza um usuário por id",
        description="Atualiza as informações de um usuário pelo id",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        operation_id="user_destroy",
        summary="Exclui um usuário pelo id",
        description="Rota para excluir as informações de um usuário pelo id",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
