from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from mysite2.forms import SignUpForm
from django.core.mail import send_mail
# from chatbot.py import greeting,response

# Views
@login_required
def landing(request):
    return render(request, "registration/landing.html", {})

def home(request):
    return render(request, "registration/home.html", {})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email= form.cleaned_data.get('email')
            user = authenticate(username = username, password = password)
            login(request, user)
            send_mail('Registration Successfull','Hello there this is to notify you....!','media06@hushmail.com',[email],
                fail_silently=False)
            return redirect('landing')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})
