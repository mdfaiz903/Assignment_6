from django.urls import path,include
from.views import local_news,International_news
urlpatterns = [
    
    path('local/', local_news,name='local_news'),
    path('int/', International_news,name='International_news'),
]
