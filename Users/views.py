from django.shortcuts import render
from Users.models import User
from Offers.models import Offer

def register_page(request):
    return render(request, 'Users/register_page.html')

def register_action(request):
    offers = Offer.objects.all().order_by('-item_name')[:10]

    if request.method == 'POST':
        user_nickname = request.POST.get('user_nickname')
        user_name = request.POST.get('user_name')
        user_surname = request.POST.get('user_surname')
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')
        date_of_birth = request.POST.get('date_of_birth')

        user = User(
            user_nickname=user_nickname,
            user_name=user_name,
            user_surname=user_surname,
            user_e_mail=user_email,
            user_password=user_password,
            date_of_birth=date_of_birth
        )
        user.save()
        return render(request, 'Core/index.html', {'offers': offers})
    return render(request, 'Core/index.html', {'offers': offers})

def login_page(request):
    return render(request, 'Users/login_page.html')

def login_action(request):
    if request.method == 'POST':
        post_user_nickname = request.POST.get('user_nickname')
        post_user_password = request.POST.get('user_password')

        user = User.objects.filter(user_nickname=post_user_nickname).first()

        if user and (post_user_password == user.user_password):
            offers = Offer.objects.all().order_by('-item_name')[:10]
            return render(request, 'Core/index.html', {'offers': offers})
        
    return render(request, 'Users/login_page.html')