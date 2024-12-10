from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
import pdb
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.validated_data)
    
class RegistrationView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            save_account = serializer.save()
            token, created = Token.objects.get_or_create(user=save_account)
            return Response({"message": "Registration successful"})

        else:
            return Response(serializer.errors)
            