from rest_framework import serializers
from .predict.predict import predict
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
class PredictionSerializer(serializers.Serializer):
    result = serializers.IntegerField()

class PredictSerializer(serializers.Serializer):
    school_level = serializers.IntegerField(max_value=2,min_value=0)
    doubts_asked = serializers.IntegerField(max_value=100,min_value=0)
    discussion   = serializers.IntegerField(max_value=100,min_value=0)
    parent       = serializers.IntegerField(max_value=1,min_value=0)
    absent       = serializers.IntegerField(max_value=1,min_value=0)

    def predict_result(self,school_level,doubts_asked,discussion,parent,absent):
        return PredictionSerializer({
            'result':  predict(school_level,doubts_asked,discussion,parent,absent)}
            )

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ('id','name','school_level','attended_classes','total_classes','discussion_score','prediction_score')

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)

    def validate_username(self,username):
        if len(User.objects.filter(username=username)) != 0:
            raise serializers.ValidationError("Username Already Exists")
        return username
    
    def save(self):
        data = self.validated_data
        user = User.objects.create_user(username=data['username'],password=data['password'])
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.save()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def validate(self,data):
        user = authenticate(username=data['username'],password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid Credentials")
        return data
    
    def get_token(self,username,password):
        user = User.objects.get(username=username)
        token, created = Token.objects.get_or_create(user=user)
        return token

class DeleteStudentSerializer(serializers.Serializer):
    sid = serializers.IntegerField()

class UpdateStudentSerializer(serializers.Serializer):
    sid = serializers.IntegerField()
    sval = serializers.IntegerField()

class ResponseSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=500)

