from django.urls import path,include
from .views import *
urlpatterns = [
    path('',indexView),
    path('dashboard/',elementsView),
    path('dashboard/add/',addView),
    path('login/',loginView),
    path('register/',registerView),
    path('dashboard/<int:pk>/',studentDetailsView),
    path('dashboard/class/',enterMarksView),
]
