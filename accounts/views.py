from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
# Create your views here.

def signup(request):
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        
    context = {'form': form}
    return render(request, 'registration/signup.html', context)
