from django.urls import path
from app16.views import * 
app_name='app16'

urlpatterns = [
    path('sample2/',sample2,name='sample2'),
]
