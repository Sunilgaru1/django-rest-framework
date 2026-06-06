from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students = [
        {'id' : 1 , 'name': 'Sunil Garu','age':19}
    ]
    return HttpResponse(students)