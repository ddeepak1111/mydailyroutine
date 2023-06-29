from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    path('progresscard/', views.progresscard, name='progresscard'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('recorddetails/<int:recordid>/', views.recorddetails, name='recorddetails'),
]
