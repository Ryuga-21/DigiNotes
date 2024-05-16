from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('This is Home Page')
    
def worksheet_list(request):
    return render(request, 'notebook_temps\worksheet_list.html')

def note_detail(request):
    return render(request, 'notebook_temps\\note_detail.html')