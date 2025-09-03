
from django.shortcuts import render

# views.py

from django.shortcuts import render, redirect  # render และ redirect
from django.contrib.auth import authenticate, login  # authenticate, login
from django.contrib import messages  # messages
from django.contrib.auth.decorators import login_required


def base(request):
	return render(request, 'base.html')

def home(request):
	return render(request, 'home.html')

def menu(request):

	return render(request, 'menu.html')


@login_required
def digitolsum_view(request):
    if request.method == "POST":
        items = []
        total_income = 0
        total_expense = 0
        i = 1
        while True:
            item = request.POST.get(f'item_{i}')
            type_ = request.POST.get(f'type_{i}')
            amount = request.POST.get(f'amount_{i}')
            if not item or not type_ or not amount:
                break
            amount = float(amount)
            items.append({
                'item': item,
                'type': type_,
                'amount': amount
            })
            if type_ == 'income':
                total_income += amount
            else:
                total_expense += amount
            i += 1
        balance = total_income - total_expense
        # ส่งข้อมูลไป slip.html
        return render(request, 'slip.html', {
            'items': items,
            'total_income': total_income,
            'total_expense': total_expense,
            'balance': balance
        })
    return render(request, 'digitolsum.html')

@login_required
def slip_view(request):
    # ถ้าเข้าตรงๆ ไม่ผ่าน POST ให้แสดง slip.html ว่าง
    return render(request, 'slip.html')

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


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, "รหัสผ่านไม่ตรงกัน")
            return render(request, 'account/register.html')
        if not username or not password1:
            messages.error(request, "กรุณากรอกข้อมูลให้ครบถ้วน")
            return render(request, 'account/register.html')
        from django.contrib.auth.models import User
        if User.objects.filter(username=username).exists():
            messages.error(request, "ชื่อผู้ใช้นี้มีอยู่แล้ว")
            return render(request, 'account/register.html')
        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        return redirect('home')
    return render(request, 'account/register.html')
