from django.contrib.auth import authenticate as auth_authenticate, login as auth_login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib import messages


from Users.models import CustomUser
from Offers.models import Offer

def register_page(request):
    return render(request, 'Users/register_page.html')

def register_action(request):
    offers = Offer.objects.all().order_by('-item_name')[:10]
    if request.method == 'POST':
        username = request.POST.get('username') #191 chars or fewer
        first_name = request.POST.get('first_name') #150 chars or fewer
        last_name = request.POST.get('last_name') #150 chars or fewer
        email = request.POST.get('email') #email address
        password = request.POST.get('password') #Password will be saved as hash
        date_of_birth = request.POST.get('date_of_birth')

        CustomUser.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,  # Django's create_user will hash the password
            date_of_birth=date_of_birth,
            is_superuser=False,
            is_staff=False,
            is_active=True,
        )

        return render(request, 'Core/index.html', {'offers': offers})

    return render(request, 'Users/register_page', {'offers': offers})


def login_page(request):
    return render(request, 'Users/login_page.html')

def login_action(request):
    print("Login action triggered")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth_authenticate(request, username=username, password=password)

        #user = CustomUser.objects.get(username=username)
        if user is not None:
        #if check_password(password, user.password):
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')

    print("Login action completed")
    return render(request, 'Users/login_page.html')