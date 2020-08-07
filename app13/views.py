from django.shortcuts import render
from app13.models import student
from app13.form import student

# Create your views here.
def index(request):
    x =student()
    # name = student(request.POST)
    # email = student(request.POST)
    return render(request, 'main.html',{'form':x})
