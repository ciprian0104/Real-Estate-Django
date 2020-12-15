from django.shortcuts import render, redirect

from django.contrib import messages, auth

from django.contrib.auth.models import User

# Create your views here.


def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        # Verificam daca parolele sunt aceleasi

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Nume de utilizator deja existent')
                return redirect('register')
            
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Emailul este deja existent')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

                # Lagam utilizatorul dupa inregistrare

                # auth.login(request, user)
                # messages.success(request, 'You are now logged in')
                # return redirect('index')

                user.save()

                messages.success(request, 'Intregistrare cu success')

                return redirect('login')

            messages.error(request, 'Parolele nu coincid')

            return redirect('register')
            
    else:
        return render(request, 'accounts/register.html')


def login(request):
    # Intram in contul specificat
    
    if request.method == 'POST':

        return None
    
    else:
        
        return render(request, 'accounts/login.html')



def logout(request):

    return redirect('index')




def dashboard(request):

    return render(request, 'accounts/dashboard.html')