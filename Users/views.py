from django.shortcuts import render
from Users.models import User

def register_page(request):
    return render(request, 'Users/register_page.html')

def register(request):
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

        return render(request, 'Core/index.html')

    return render(request, 'Core/index.html')






