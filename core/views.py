from django.contrib.auth import get_user_model, authenticate
from django.shortcuts import render
from models import User
# Create your views here.


def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and passowrd:

            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('success', user)

            else:
                messages.error(request, 'Username or Password is Incorrect')

        else:
            messages.error(request, 'fill out all the fields')

    return render(request, 'web/login1.html', {})
