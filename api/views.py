from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions
from .serializers import *
from rest_framework.response import Response
# Create your views here.

class PredictView(generics.GenericAPIView):
    serializer_class = PredictSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self,request):
        self.serializer = self.get_serializer(data=request.data)
        self.serializer.is_valid(raise_exception=True)
        r = self.serializer.predict_result(request.data['school_level'],request.data['doubts_asked'],request.data['discussion'],request.data['parent'],request.data['absent'])
        return Response(r.data,status.HTTP_200_OK)