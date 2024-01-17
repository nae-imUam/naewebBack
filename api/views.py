from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import viewsets, serializers, status
from django.contrib.auth.tokens import default_token_generator
from rest_framework.response import Response
from .models import UserProfile, UserData, MiniTest
from .serializers import MiniTestSerializer
from django.views.decorators.http import require_GET
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response




def generate_token(user):
    return default_token_generator.make_token(user)



@require_GET
def check_username_availability(request, username):
    try:
        user = User.objects.get(username=username)
        return JsonResponse({'available': False})
    except User.DoesNotExist:
        return JsonResponse({'available': True})
    
    
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        phone = data.get('phone')
        name = data.get('name')
        password = data.get('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        UserData.objects.create(username=username, email=email, password=password)
        UserProfile.objects.create(user=user, phone=phone, name=name)

        # Return user information in the response
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'phone': phone,  # Include other UserProfile fields if needed
            'name': name,
        }

        return JsonResponse({'message': 'Signup successful', 'user': user_data}, status=201)

    return JsonResponse({'message': 'Invalid request method'}, status=400)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            # Assuming you have a function to generate a token for the user
            token = generate_token(user)
            return JsonResponse({'token': token, 'user': {'username': user.username}}, status=200)

        return JsonResponse({'message': 'Invalid credentials'}, status=401)

    return JsonResponse({'message': 'Invalid request method'}, status=400)


class MiniTestViewSet(viewsets.ModelViewSet):
    queryset = MiniTest.objects.all()
    serializer_class = MiniTestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        # Check serializer validation
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



@api_view(['GET'])
def get_minitest_by_test_number(request, test_number):
    minitest = get_object_or_404(MiniTest, test_number=test_number)
    serializer = MiniTestSerializer(minitest)
    return Response(serializer.data)