from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    # 로그인 체크
    print("안녕하세요")
    if me: # 로그인 상태 : newsfeed 페이지 이동
        return redirect('/')
    else: # 로그아웃 상태 : signin 페이지로 이동
        return render(request, '/user/signin.html/')

def main(request):
    return render(request, 'user/signin.html/') # 로그인