from django.shortcuts import render
from Users.models import User
import sys

def index(request):
    return render(request, 'Core/index.html', {})

#def index(request):
#    users = User.objects.all().order_by('-date_of_birth')[:6]
#    return render(request, 'Core/index.html', {'users': users})
