from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions
from .serializers import *
from rest_framework.response import Response
from .models import *
# Create your views here.

class PredictView(generics.GenericAPIView):
    serializer_class = PredictSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self,request):
        self.serializer = self.get_serializer(data=request.data)
        self.serializer.is_valid(raise_exception=True)
        r = self.serializer.predict_result(request.data['school_level'],request.data['doubts_asked'],request.data['discussion'],request.data['parent'],request.data['absent'])
        return Response(r.data,status.HTTP_200_OK)

class StudentsGetView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return student.objects.filter(mentor=self.request.user)
    def post(self,request):
        data = request.data
        student.objects.create(mentor=request.user,name=data['name'],school_level=data['school_level'],attended_classes=data['attended_classes'],total_classes=data['total_classes'],discussion_score=data['discussion_score'],prediction_score=data['prediction_score'])
        response = ResponseSerializer({
            'message' : 'success'
        })
        return Response(response.data,status.HTTP_200_OK)

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)
    def post(self,request):
        self.serializer = self.get_serializer(data=request.data)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        response = ResponseSerializer({'message':'success'})
        return Response(response.data,status.HTTP_200_OK)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)
    def post(self,request):
        self.serializer = self.get_serializer(data=request.data)
        self.serializer.is_valid(raise_exception=True)
        token = self.serializer.get_token(request.data['username'],request.data['password'])
        response = ResponseSerializer({'message':token})
        return Response(response.data,status.HTTP_200_OK)