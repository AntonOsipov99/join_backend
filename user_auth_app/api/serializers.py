
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from rest_framework.authtoken.models import Token

        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data['email']
        password = data['password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")

        if user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return {'token': token.key, 'username': user.username}
        else:
            raise serializers.ValidationError("Incorrect password")

username_validator = RegexValidator(
    regex=r'^[\w\s]+$',  # Erlaubt Buchstaben, Zahlen, Unterstriche und Leerzeichen
    message='Enter a valid username. This value may contain letters, numbers, underscores, and spaces.',
    code='invalid_username'
)
class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only= True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'validators': [username_validator]}
        }
        
    def save(self):
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']
        
        if pw != repeated_pw:
            raise serializers.ValidationError({'error': 'passwords dont match'})
        
        account = User(username=self.validated_data['username'], email=self.validated_data['email'])
        account.set_password(pw)
        account.save()
        return account