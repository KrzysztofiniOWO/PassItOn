from django.shortcuts import render
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

# def login_page(request):
#     return render(request, 'Users/login_page.html')

# def login_action(request):
#     if request.method == 'POST':
#         post_user_nickname = request.POST.get('user_nickname')
#         post_user_password = request.POST.get('user_password')

#         user = User.objects.filter(user_nickname=post_user_nickname).first()

#         if user and (post_user_password == user.user_password):
#             offers = Offer.objects.all().order_by('-item_name')[:10]
#             return render(request, 'Core/index.html', {'offers': offers})
        
#     return render(request, 'Users/login_page.html')