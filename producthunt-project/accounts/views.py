from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

class ShowAccountsPage():

    def show_signup(request):
        if request.method == 'POST':
            if request.POST['username'] == '' or request.POST['password'] == ''  or request.POST['password-confirm'] =='':
                messages.add_message(request, messages.INFO, 'Please do not leave any feild empty, all three fields are required for signing up!')
            else:
                if ShowAccountsPage.examine_user_input(request) == True:
                    return redirect('home')
        return render(request, 'accounts/signup.html')

    def show_login(request):

        if request.method == 'POST':
            user = auth.authenticate(username=request.POST['username'], password= request.POST['password'])

            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.add_message(request, messages.INFO, 'Username or password is incorrect.')
                return render(request, 'accounts/login.html') 

        return render(request, 'accounts/login.html')

    def show_logout(request):
        if request.method == 'POST':
            auth.logout(request)
            return redirect('home')

    def examine_user_input(request):
        try:
            user = User.objects.get(username=request.POST['username'])
            messages.add_message(request, messages.ERROR,'Username has been already taken, please try another username.')
        except:
            if request.POST['password'] == request.POST['password-confirm']:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                print("@@@@@@@ A new user has been created")
                return True
            else:
                messages.add_message(request, messages.INFO,'Passwords must match!')
#https://www.programcreek.com/python/example/74718/django.core.validators.EmailValidator
    def is_email(request):
        from django.core.exceptions import ValidationError
        from django.core.validators import EmailValidator

        validator = EmailValidator()
        try:
            validator(request.POST['email'])
        except ValidationError:
            show_message('email format is not valid!')
            return False

        return True

    def show_message(msg):
        messages.add_message(request, messages.INFO,msg)