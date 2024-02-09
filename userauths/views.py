from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect


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



def LoginView(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are login!')
        return redirect('core:home')
    
    if request.method=='POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.warning(request, 'You are logged in')
                return redirect("core:home")
            else:
                messages.error(request, "Username or password dosen't match")
                return redirect("userauths:sign-in")
        except:
            messages.error(request, "User doesn't exists")
    return HttpResponseRedirect('/')