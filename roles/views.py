from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Roles
from .serializers import *


# Create your views here.

@api_view(['GET'])
def index(request):
    data = Roles.objects.all().order_by('-id')
    serializer = RolesSerializers(data, context={'request': request}, many=True)
    return Response({"message": "Success", "data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def store(request):
    libelle = request.data.get('libelle')
    description = request.data.get('description')
    created_at = request.data.get('created_at')
    serializer = RolesSerializers(data={
        'libelle': libelle,
        'description': description,
        'created_at': created_at,
    })
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Enregistrement effectuée avec succès.", "data": serializer.data},
                        status=status.HTTP_201_CREATED)
    return Response({"message": "Erreur lors de l'enregistrement.", "data": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update(request, id):
    try:
        role = Roles.objects.get(id=id)
    except Roles.DoesNotExist:
        return Response({"message": "Le rôle n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

    libelle = request.data.get('libelle')
    description = request.data.get('description')
    updated_at = request.data.get('updated_at')

    serializer = RolesSerializers(role, data={
        'libelle': libelle,
        'description': description,
        'updated_at': updated_at,
    }, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Mise à jour effectuée avec succès.", "data": serializer.data},
                        status=status.HTTP_200_OK)
    return Response({"message": "Erreur lors de la mise à jour.", "data": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, id):
    try:
        role = Roles.objects.get(id=id)
    except Roles.DoesNotExist:
        return Response({"message": "Le rôle n'existe pas."}, status=status.HTTP_404_NOT_FOUND)

    role.delete()
    return Response({"message": "Suppression effectuée avec succès."}, status=status.HTTP_204_NO_CONTENT)