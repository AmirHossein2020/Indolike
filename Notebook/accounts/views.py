from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm
# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home') 
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form': form})
