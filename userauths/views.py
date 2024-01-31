from django.shortcuts import render
from django.contrib import messages

from forms import UserCreationForm


class RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are registered!')
        return render('core:feed')
    
    form = UserCreationForm(request.POST or None)
