from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Data
from .serializers import DataSerializer

@api_view(['GET'])
def getData(request):
    # getdata from api

    app = Data.objects.all()
    serializer = DataSerializer(app, many=True)

    return Response(serializer.data)
