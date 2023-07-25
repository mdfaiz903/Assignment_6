from django.shortcuts import render

# Create your views here.
def local_news(request):
    return render(request,'Sports/local.html')

def International_news(request):
    return render(request,'Sports/international.html')