from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import RegistrationSerializer, LoginSerializer, ChangePasswordSerializer

class RegisterUser(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": f"{user.username} registration successful", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                return Response({"message": f"{user.username} logged in successfully", "data": {"username": user.username, "email": user.email}}, status=status.HTTP_200_OK)
            else:
                return Response({"message": f"Sorry, {username} is not registered. Please register first. or check your password"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePassword(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            user = authenticate(username=username, password=old_password)
            if user:
                user.set_password(new_password)
                user.save()
                return Response({"message": f"{user.username} password changed successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid credentials. Please check your username and old password."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
