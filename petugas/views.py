from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

from petugas.models import Petugas

# Create your views here.
def login_to_sys(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                try:
                    akun = Petugas.objects.get(username=user.id)
                    login(request, user)
                    request.session['username'] = request.POST['username']
                    request.session['nama'] = akun.nama_depan
                    request.session['id'] = akun.id
                    request.session['hak'] = akun.hak
                except:
                    messages.add_message(request, messages.INFO, 'Login gagal :(')
                return redirect('/')
            else:
                messages.add_message(request, messages.INFO, 'Login gagal')
        else:
            messages.add_message(request, messages.INFO, 'Username atau password Anda salah')
    return render(request, 'login.html')

@login_required(login_url=settings.LOGIN_URL)
def logout_from_sys(request):
    logout(request)
    return redirect('/login/')
