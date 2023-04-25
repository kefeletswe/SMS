from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
  return render(request, 'students/home.html', {
    'students': Student.objects.all()
  })