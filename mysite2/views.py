from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from mysite2.forms import SignUpForm
# from chatbot.py import greeting,response

# Views
@login_required
def landing(request):
    return render(request, "landing.html", {})

def home(request):
    return render(request, "home.html", {})

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
            return redirect('landing')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})



# def index(request):
#     return render(request, 'registration/index.html',{})