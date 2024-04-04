from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
def login_views(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('second_password')
        else:
            error_message = 'Login gagal, Masukkan Password dan Username dengan tepat!!!'
    return render(request, 'login.html', {'error_message': error_message})
@login_required
def second_password(request):
    error_message = None
    if request.method == 'POST':
        second_password = request.POST.get('second_password')
        if second_password == 'Riswan2904':
            return redirect('dashboard')
        else:
            error_message = 'Kamu bukan Riswan Kan  Ya.... JUJURRRRR'
    return render(request, 'second_password.html', {'error_message': error_message})
def home(request):
    return render (request, 'index.html')

