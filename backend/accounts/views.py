from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import RegisterSerializer, EmailLoginSerializer, PlayerSerializer
from .models import Player
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
class EmailLoginView(APIView):
    serializer_class = EmailLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            # Aqui você pode retornar um token ou os dados do usuário
            # return Response({"message": "Login realizado com sucesso."})
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PlayerView(APIView):
    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            player = serializer.save()
            return Response(PlayerSerializer(player).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterUserPlayerView(APIView):
    def post(self, request):
        user_data = request.data.get('user')
        player_data = request.data.get('player')

        if not user_data or not player_data:
            return Response({"error": "User and Player data are required."}, status=status.HTTP_400_BAD_REQUEST)

        user_serializer = RegisterSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            player_data['username'] = user.username  # Link the player to the created user's username
            player_serializer = PlayerSerializer(data=player_data)
            if player_serializer.is_valid():
                player = player_serializer.save()
                return Response({
                    "user": RegisterSerializer(user).data,
                    "player": PlayerSerializer(player).data
                }, status=status.HTTP_201_CREATED)
            else:
                user.delete()  # Rollback user creation if player creation fails
                return Response(player_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)