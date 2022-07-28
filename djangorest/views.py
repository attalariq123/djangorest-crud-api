from telnetlib import STATUS
from django.http import JsonResponse
from .models import Mahasiswa
from .serializers import MahasiswaSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions

from djangorest import serializers

class MahasiswaViewSet(viewsets.ModelViewSet):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializers
    permission_classes = [permissions.IsAuthenticated]

# @api_view(['GET', 'POST'])
# def mahasiswa_list(request, format=None):

#     if request.method == 'GET':
#         mahasiswa = Mahasiswa.objects.all()
#         serializer = MahasiswaSerializers(mahasiswa, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MahasiswaSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'PUT', 'DELETE'])
# def mahasiswa_detail(request, id, format=None):

#     try:
#         mahasiswa = Mahasiswa.objects.get(pk=id)
#     except Mahasiswa.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':    
#         serializer = MahasiswaSerializers(mahasiswa)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = MahasiswaSerializers(mahasiswa, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         mahasiswa.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)