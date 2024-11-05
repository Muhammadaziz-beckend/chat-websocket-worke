from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from chat.models import Room, Message
from .serializers import RoomSerializer, MessageSerializer
from rest_framework.permissions import *

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]  # Require authentication

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            return Response({'detail': 'Authentication required.'}, status=status.HTTP_403_FORBIDDEN)
