from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Hood, Profile, Business

# Create your views here.
def index(request):
 
    return render(request, 'index.html')    
