from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, UserRefreshToken

class UserRefreshTokenSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  

    class Meta:
        model = UserRefreshToken
        fields = ['user', 'token', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    """Serializer de base pour les infos du modèle User"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer principal pour le profil utilisateur"""
    user = UserSerializer(read_only=True)  # informations liées à User (imbriquées)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True, required=False
    )

    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user',         # affichage lecture
            'user_id',      # en écriture
            'photo',
            'telephone',
            'adresse',
            'role',
            'created_at',
            'update_at',
        ]
        read_only_fields = ['created_at', 'update_at']
