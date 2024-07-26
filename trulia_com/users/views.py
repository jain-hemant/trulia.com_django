from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import *
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]


