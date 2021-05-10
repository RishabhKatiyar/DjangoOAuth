from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    model = User

    def list(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)