from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    data = request.data
    user = User.objects.create(phone=data['phone'], name=data['name'], role=data['role'])
    user.set_password(data["password"])
    user.save()
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
