from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model    

User = get_user_model()
    
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
            
class EmailCheckView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        email = request.data.get('email')
        
        if not email:
            return Response(
                {"error": "Email is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        user_exists = User.objects.filter(email=email).exists()
        
        if user_exists:
            return Response(
                {"email": email},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "User with this email not found"},
                status=status.HTTP_404_NOT_FOUND
            )