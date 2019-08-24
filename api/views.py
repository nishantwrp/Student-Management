from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions
from .serializers import *
from .predict.predict import predict
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

class DeleteStudentView(generics.GenericAPIView):
    serializer_class = DeleteStudentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def post(self,request):
        student.objects.filter(id=request.data['sid']).delete()
        response = ResponseSerializer({
            'message' : 'success'
        })
        return Response(response.data,status.HTTP_200_OK)

class UpdateStudentView(generics.GenericAPIView):
    serializer_class = UpdateStudentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def post(self,request):
        x = student.objects.get(id=int(request.data['sid']))
        sum_avg = x.discussion_score*x.total_classes
        sum_avg += int(request.data['sval'])
        x.total_classes += 1
        x.discussion_score = int(sum_avg/x.total_classes)
        if int(request.data['sval']) != 0:
            x.attended_classes += 1
        x.save()
        absent = 0
        if (x.attended_classes/x.total_classes) < 0.9:
            absent = 1
        if absent == 0 and x.discussion_score >= 50:
            x.prediction_score = 2
        else:
            x.prediction_score = min(predict(x.school_level,x.discussion_score/3,0,0,1),predict(x.school_level,0,x.discussion_score/3,0,1)) - 1
        x.save()
        response = ResponseSerializer({
            'message': 'success'
        })
        return Response(response.data,status.HTTP_200_OK)

         