from django.urls import path,include
from.views import entertainment
urlpatterns = [
    
    path('ent/', entertainment,name='entertainment'),
   
]


