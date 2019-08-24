from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import *
schema_view = get_schema_view(
   openapi.Info(
      title="Student Management API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('',schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('predict/',PredictView.as_view()),
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('students/',StudentsGetView.as_view()),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'), 
] 
