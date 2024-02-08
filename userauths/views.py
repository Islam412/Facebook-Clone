from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from userauths.forms import UserRegisterForm
from userauths.models import Profile


def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are registered!')
        return redirect('core:home')
    
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        
        full_name = form.cleaned_data.get('full_name')
        phone = form.cleaned_data.get('phone')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = authenticate(email=email, password=password)
        login(request, user)

        profile = Profile.objects.create(user=user, full_name=full_name, phone=phone)
        
        messages.success(request, f'Hi {full_name}. Your account was created successfully.')
        return redirect('core:home')
    
    context = {
        'form': form
    }
    return render(request, 'userauths/sign-up.html', context)