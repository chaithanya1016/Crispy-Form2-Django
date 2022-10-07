from django.shortcuts import render
from .forms import SignupForm

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form':form})

