from django.urls import path,include
from.views import educations
urlpatterns = [
    
    path('edu/', educations,name='educations'),
   
]


