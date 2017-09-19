from django.shortcuts import render
from django.http import HttpResponseRedirect
from CardSystem import models


# 首页
def index(request):
    # 若已登录则显示欢迎信息
    message = request.session.get('message', '')
    params = {}
    if message != '':
        params['message'] = message
        del request.session['message']
    return render(request, 'CardSystem/index.html', params)


# 登录页面
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        is_matched = models.Users.objects.filter(username=username, password=password)
        if is_matched:
            request.session['login_user'] = username
            request.session['message'] = 'welcome, ' + username
            return HttpResponseRedirect('/index')
        else:
            # 服务器端加上判断, 防止绕过js发送请求
            # ...判断语句...
            return render(request, 'CardSystem/index.html')
    else:
        return render(request, 'CardSystem/login.html')


# 注册页面
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        # 检测输入的合法性 [缺少长度和字符组成判断]
        if username == '':
            return render(request, 'CardSystem/register.html')
        else:
            is_exist = models.Users.objects.filter(username=username)   # 判断用户名是否已经存在
            if is_exist:
                return render(request, 'CardSystem/register.html')
            else:
                if password == '':                                      # 判断密码是否为空
                    return render(request, 'CardSystem/register.html')
                elif password != password2:                             # 判断两次输入的密码是否一致
                    return render(request, 'CardSystem/register.html')
                else:                                                   # 输入合法, 将数据插入数据表
                    models.Users.objects.create(username=username, password=password)
                    # request.session['message'] = 'register successfully!'
                    return HttpResponseRedirect('/login')
    else:
        return render(request, 'CardSystem/register.html')
