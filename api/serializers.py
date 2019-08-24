from rest_framework import serializers
from .predict.predict import predict

class PredictionSerializer(serializers.Serializer):
    result = serializers.IntegerField()

class PredictSerializer(serializers.Serializer):
    school_level = serializers.IntegerField()
    doubts_asked = serializers.IntegerField()
    discussion   = serializers.IntegerField()
    parent       = serializers.IntegerField()
    absent       = serializers.IntegerField()

    def predict_result(self,school_level,doubts_asked,discussion,parent,absent):
        return PredictionSerializer({
            'result':  predict(school_level,doubts_asked,discussion,parent,absent)}
            )