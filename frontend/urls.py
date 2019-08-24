from django.urls import path,include
from .views import *
urlpatterns = [
    path('',indexView),
    path('dashboard/',elementsView),
    path('generic/',genView),
    path('login/',loginView),
    path('register/',registerView),
]
