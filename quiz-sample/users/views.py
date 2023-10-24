from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create y our views here.
def register(request):
    """
    view function for user registration
    """
    # if this a post request, process form data
    if request.method == 'POST':
        # create form instance & populate with data from request binding
        form = UserRegisterForm(request.POST)

        # check if the form is valid
        if form.is_valid():
            # process the data in a cleaned_data (to the username)
            form.save()
            username = form.cleaned_data['username']
            messages.success(
                request, f'Account created for {username}!, you can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
