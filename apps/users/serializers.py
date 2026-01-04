from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', 'is_staff', 'is_superuser', 'date_joined','last_login']


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=128,  write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'email', 'first_name', 'last_name']
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('password and confirm_password are not the same value.')
        
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')

        user = User(**validated_data)   
        user.set_password(password)
        user.save()

        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)