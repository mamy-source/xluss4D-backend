from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserRefreshToken
from .serializers import UserRefreshTokenSerializer


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Création de l'utilisateur
        user = User.objects.create_user(username=username, password=password, email=email)

        # Génération du token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Sauvegarder ou mettre à jour le refresh token en base
        refresh_token_obj, _ = UserRefreshToken.objects.update_or_create(
            user=user,
            defaults={'token': refresh_token}
        )

        # Sérialisation du refresh token
        refresh_token_data = UserRefreshTokenSerializer(refresh_token_obj).data

        # Réponse
        return Response({
            'access': access_token,
            'refresh': refresh_token_data
        }, status=status.HTTP_201_CREATED)