from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import Data
from .serializers import DataSerializer


class TaskListApiView(APIView):
    # Task list API

    # add permission to check if the user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''List all tasks'''

        tasks = Data.objects.all()
        serializer = DataSerializer(tasks, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''

        data = {
            'task_name': request.data.get('task_name'),
            'task_description': request.data.get('task_description'),
            'completed': request.data.get('completed'),
            'updated': request.data.get('updated'),
        }
        serializer = DataSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
'''
@api_view(['GET'])
def getData(request):
    # getdata from api

    app = Data.objects.all()
    serializer = DataSerializer(app, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    # post data into the api

    data = {
        'task_name': request.data.get('task_name'),
        'task_description': request.data.get('task_description'),
        'completed': request.data.get('completed'),
        'updated': request.data.get('updated'),
    }
    serializer = DataSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()

    return(serializer.data)
'''