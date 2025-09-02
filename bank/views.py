
from django.shortcuts import render

# views.py
from django.shortcuts import render, redirect  # render และ redirect
from django.contrib.auth import authenticate, login  # authenticate, login
from django.contrib import messages  # messages


def base(request):
	return render(request, 'base.html')

def home(request):
	return render(request, 'home.html')

def menu(request):

	return render(request, 'menu.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # เปลี่ยนเป็นชื่อ URL หน้า Home ของคุณ
        else:
            messages.error(request, "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
    return render(request, 'account/login.html')
