from rest_framework.serializers import Serializer
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from .tasks import send_email_task

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def list(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # Celery code here
        send_email_task.delay(request.data['email'], request.data['username'])        
        return Response(serializer.data)