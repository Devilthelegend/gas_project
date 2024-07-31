# gas_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Request
from .forms import RequestForm, SignUpForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.decorators.http import require_POST


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('user_requests')
    else:
        form = SignUpForm()
    return render(request, 'gas_app/sign_up.html', {'form': form})

@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user
            new_request.save()
            return redirect('user_requests')
    else:
        form = RequestForm()
    return render(request, 'gas_app/create_request.html', {'form': form})

@login_required
def user_requests(request):
    requests = Request.objects.filter(user=request.user)
    return render(request, 'gas_app/user_requests.html', {'requests': requests})

@user_passes_test(lambda u: u.is_staff)
def support_dashboard(request):
    all_requests = Request.objects.all()
    return render(request, 'gas_app/support_dashboard.html', {'requests': all_requests})
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
from django.contrib.auth import logout
from django.shortcuts import redirect

@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')