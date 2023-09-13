from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import StudentSerializer
from rest_framework import status


@api_view(['GET','POST','PUT','DELETE'])
def studentapi(request,pk=None):
  if request.method == 'GET':
      # id = request.data.get('id')
      id = pk
      if id is not None:
          stu = Student.objects.get(pk=id)
          print(stu)
          serializer = StudentSerializer(stu)
      else :
          stu = Student.objects.all()
          print(stu)
          serializer = StudentSerializer(stu , many=True)
      return Response(serializer.data)

  if request.method == 'POST':
    serializer = StudentSerializer(data = request.data)
    if serializer.is_valid():
       serializer.save()
       return Response({'msg':'Data Created'} , status=status.HTTP_201_CREATED ) # Created
    return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
  
  if request.method == 'PUT':
    # id = request.data.get('id')
    id = pk
    stu = Student.objects.get(pk=id)
    serializer = StudentSerializer(stu, data=request.data, partial = True)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Data Updated'})
    return Response(serializer.errors)
  
  if request.method == 'DELETE':
    # id = request.data.get('id')
    id = pk
    stu = Student.objects.get(pk=id)
    stu.delete()
    return Response({'msg':'Data Deleted'})
      
      
