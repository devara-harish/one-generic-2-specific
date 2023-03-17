from django.urls import path
from app17.views import * 
app_name='app17'

urlpatterns = [
    path('sample3/',sample3,name='sample3'),
]
