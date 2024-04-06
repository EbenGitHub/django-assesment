from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .decorators import role_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from .serializer import UserSerializer, LoginSerializer, ChangePasswordSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required
def home(request):
    return render(request, "registration/success.html", {})

# authentication routes
@extend_schema(request=UserSerializer)
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
@extend_schema(request=LoginSerializer)
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')   
    print(email, password) 
    try: 
        user = authenticate(request, email=email, password=password)
        print('user is' + user)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=status.HTTP_200_OK)
    except:
        return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
def logout(request):
    try:
        logout(request)
        return JsonResponse({'message': 'Logout successful'}, status=status.HTTP_200_OK)
    except:
        return JsonResponse({'error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
    
@extend_schema(request=ChangePasswordSerializer)
@api_view(['POST'])
def change_password(request):
    serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# user routes

@login_required
@api_view(['GET'])
def profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response({'user': serializer.data}, status=status.HTTP_200_OK)

@login_required
@role_required('admin')
@api_view(['GET'])
def user_lists(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    print(users)
    return Response({'users': serializer.data}, status=status.HTTP_200_OK)