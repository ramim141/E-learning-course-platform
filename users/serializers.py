from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser


# [P1-UR-1] Standard Registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'password']
    
    def create(self, validated_data):
        user  = CustomUser.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
            is_active=False
        )
        return user


# Custom Token Obtain Pair Serializer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        if not self.user.is_verified:
            raise serializers.ValidationError({
                "detail": "Account not verified. Please check your email."
            })
            
        
        data['user'] = {
            'id': self.user.id,
            'email': self.user.email,
            'name': self.user.name,
            'role': self.user.role,
        }
        return data



# [P1-UR-4] Basic Profile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'email', 'profile_picture', 'role')
        read_only_fields = ('role', 'email')

# [P1-UR-3] Password Reset Serializers
class RequestPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

class ConfirmPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True)