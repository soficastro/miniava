from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm,
    SetPasswordForm)
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings

from miniava.core.utils import generate_hash_key

from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset
from miniava.accounts import templates
from miniava.courses.models import Enrollment

from miniava.courses.models import Enrollment

User = get_user_model

@login_required
def dashboard(request):
	template_name = 'dashboard.html'
	context = {}
	return render(request, template_name, context)

def register(request):
	template_name = 'register.html'
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(
				username=user.username, 
				password=form.cleaned_data['password1']
			)
			login(request, user)
			return redirect('/')

	else:
		form = RegisterForm()
	context = {
		'form': form
	}
	return render(request, template_name, context)


def password_reset(request):
    template_name = 'password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

def password_reset_confirm(request, key):
    template_name = 'password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)
