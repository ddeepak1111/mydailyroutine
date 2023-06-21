from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    # Other URL patterns for the record app
    
    # Progress Card URL
    path('progresscard/', views.progresscard, name='progresscard'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('recorddetails/<int:recordid>/', views.recorddetails, name='recorddetails'),
]
