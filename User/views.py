from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(APIView):

    permission_classes = [AllowAny]
    def post(self, request):

        serializer = RegisterSerializer(data = request.data)

        if serializer.is_valid():
            user = serializer.save()
            response = {
                "message": "Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi.",
                "user_id": user.id,
                "username": user.username
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = LoginSerializer(data = request.data)

        if serializer.is_valid():
            
            user = serializer.validated_data.get('user')
            refresh = RefreshToken.for_user(user = user)

            response = {
                "access_token":str(refresh.access_token),
                "refresh_token":str(refresh)
            }

            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)