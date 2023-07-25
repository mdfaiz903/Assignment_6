from django.shortcuts import render

# Create your views here.
def educations(request):
    return render(request,'Educations/edu.html')