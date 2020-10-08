from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.mail import EmailMessage

from django.contrib.auth import get_user_model

User = get_user_model()

from mapapp.models import latlng
from accounts.models import UserProfile


def register(request):
    if request.method == 'POST':
        # Get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        organization = request.POST['organization']
        country = request.POST['country']
        city = request.POST['city']
        department = request.POST['department']
        address = request.POST['address']
        phone = request.POST['phone']

        # Check if passwords match
        if password == password2:
            # TODO: DO VALIDATIONS HERE
            
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is already being used!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    organization=organization, country=country, city=city,
                                                    department=department, address=address, phone=phone)
                    # auth.login(request, user){% block content %}

                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # Login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('dashboard')

    return render(request, 'accounts/login.html')


def dashboard(request):
    featured_works = latlng.objects.order_by('-request_date')

    context = {
        'features': featured_works
    }
    return render(request, 'accounts/dashboard.html', context)


def mailGun(request):
    if request.method == 'POST':
        # Get form values
        usernameTouch = request.POST['usernameTouch']
        emailTouch = request.POST['emailTouch']
        subjectTouch = request.POST['subjectTouch']
        bodyTouch = request.POST['bodyTouch']
        print(usernameTouch, emailTouch, subjectTouch, bodyTouch)

        msg = EmailMessage(
            subjectTouch,
            bodyTouch,
            emailTouch,
            ['tsegupower@gmail.com'],
        )
        msg.content_subtype = "html"
        msg.send()
        messages.success(request, 'Dear ' + usernameTouch + ', Great! We will be in contact soon.')
        return render(request, 'accounts/dashboard.html')

    return render(request, 'accounts/dashboard.html')
