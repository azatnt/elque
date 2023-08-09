from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from appeals.models import Appeal
from users.models import User


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_appeal(request):
    data = request.data
    user = request.user

    Appeal.objects.create(user=user, topic=data['topic'], description=data['description'])
    return Response({'message': 'Appeal created successfully'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rector_clients(request):
    user = request.user

    if user.role != User.Names.RECTOR:
        return Response({'message': 'You are not authorized to create this type of appeal'},
                        status=status.HTTP_403_FORBIDDEN)

    queryset = Appeal.objects.filter(topic=Appeal.Topics.RECTOR, is_completed=False)
    return Response(queryset.values(), status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def complete_appeal(request):
    data = request.data
    user = request.user

    if user.role != User.Names.SECRETARY:
        return Response({'message': 'You are not authorized to create this type of appeal'},
                        status=status.HTTP_403_FORBIDDEN)

    Appeal.objects.filter(id=data["appeal_id"]).update(is_completed=True)
    return Response({'message': 'Appeal successfully updated'}, status=status.HTTP_200_OK)
