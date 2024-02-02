from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login

from userauths.forms import UserCreationForm
from userauths.models import Profile


class RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are registered!')
        return render(request, 'core:home')
    
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        full_name = form.cleaned_data.get('full_name')
        phone = form.cleaned_data.get('phone')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = authenticate(email=email,password=password)
        login(request, user)

        
        profile = Profile.objects.get(user=request.user)
        profile.full_name = full_name
        profile.phone = phone
        profile.save()

        messages.success(request,f'Hi {full_name}. Your account was created successfully.')
        return render(request, 'core:home')
    
    context = {
        'form':form
    }
    return render(request, 'userauths/sign-up.html',context)