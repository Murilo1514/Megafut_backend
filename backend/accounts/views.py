from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import RegisterSerializer, EmailLoginSerializer
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