from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login     # 밑에 정의된 login과 구별하기 위해
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def signup(request):
    # 로그인 유무 판별 & 로그인된 경우 redirect
    if request.user.is_authenticated:
        return redirect('elec:index')

    if request.method == 'POST':
        # 실제 회원 생성
        # 1. 넘어온 데이터를 Form Class에 입력하기
        form = UserCreationForm(request.POST)

        # 2. 유효한 값인지 검증
        if form.is_valid():
            # 3. 회원 생성!
            user = form.save()
            # 3-1. 로그인!
            auth_login(request, user)
            # 4. redirect -> 마이페이지 (elec index)
            return redirect('elec:index')
    else:
        # 회원 가입 양식 보여줌
        form = UserCreationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    # 로그인 유무 판별 & 로그인된 경우 redirect
    if request.user.is_authenticated:
        return redirect('elec:index')

    if request.method == 'POST':
        # 로그인
        # 1. POSt 요청으로 넘어온 데이터를 Form에 입력
        form = AuthenticationForm(request, request.POST)

        # 2. 검증
        if form.is_valid():
            # 3. 로그인 수행
            auth_login(request, form.get_user())
            # 4. redirect -> 메인 페이지 (elec index)
            # 4-1. next 값 가져오기
            next = request.GET.get('next')
            return redirect(next or 'elec:index')       # next값이 있다면 로그인 후 next 주소로 돌아감
    else:
        # 로그인 창 보여줌
        form = AuthenticationForm()
    
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

# Signup vs. Login
# 1. Signup
# User를 Create

# 2. Login
# Session을 Create

# 3. Logout
# Session을 Delete


# Session이란?
# Django가 브라우저의 정보를 가져와
# 임시로 들고 있도록 해서
# 지금 이 페이지를 보는 User가 누구인지
# 서버쪽에서 정보를 들고 있는 것.

# POST 요청만 받음
def logout(request):
    if request.method == 'POST':
        # 로그아웃 수행
        auth_logout(request)
        return redirect('elec:index')

def edit(request):
    if request.method == 'POST':
        # 회원 정보 수정
        # 1. POST로 넘어온 데이터 Form에 입력
        form = CustomUserChangeForm(request.POST, instance=request.user)

        # 2. 검증
        if form.is_valid():
            # 3. 저장
            form.save()
            # 4. redirect -> 메인 (elec index)
            return redirect('elec:index')
    else:
        # 회원 정보 수정 Form 보여줌
        form = CustomUserChangeForm(instance=request.user)  # 현재 값 자동으로 채워져 있음

    context = {
        'form' : form,
    }
    return render(request, 'accounts/edit.html', context)

# POST 요청만 받음
def delete(request):
    if request.method == 'POST':
        # User 삭제
        request.user.delete()
        return redirect('elec:index')

def password(request):
    if request.method == 'POST':
        # 실제로 비밀번호 변경
        # 1. 넘어온 데이터 Form에 입력
        form = PasswordChangeForm(request.user, request.POST)
        # 2. 검증
        if form.is_valid():
            # 3. 비밀번호 저장
            user = form.save()
            # 3-1. 세션 유지 (로그인 유지)
            update_session_auth_hash(request, user)
            # 4. redirect -> 메인 페이지
            return redirect('elec:index')
    else:
        # 비밀번호를 변경하는 양식 보여줌
        form = PasswordChangeForm(request.user)

    context = {
        'form' : form,
    }
    return render(request, 'accounts/password.html', context)
