from django.shortcuts import render
import requests
# Create your views here.

def indexView(request):
    headers = {
        "Authorization": "Token 94ffe6b9d767055e0abcb351d8cd46c2ac2ed1bf"
    }
    data = {
  "name": "string",
  "school_level": 0,
  "attended_classes": 0,
  "total_classes": 0,
  "discussion_score": 0,
  "prediction_score": 0
}
    r = requests.post(url='http://127.0.0.1:8000/api/students/',headers=headers,data=data)
    print(r.json())
    return render(request,'index.html')