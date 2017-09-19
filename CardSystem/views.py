from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from CardSystem import models
from django.views.decorators.csrf import csrf_exempt
import re
# **** 一些共享变量 ****
name_regex = r'[a-zA-Z0-9]{6,18}'
pass_regex = r'[\w\W]{8,18}'
check_name = re.compile(name_regex)
check_pass = re.compile(pass_regex)
# **** 一些共享变量 ****



# 首页
# [最终要修改成显示名片列表信息]
# 目前只显示欢迎信息
def index(request):
    # 若已登录则显示欢迎信息
    message = request.session.get('message', '')
    params = {}
    if message != '':
        params['message'] = message
        del request.session['message']
    return render(request, 'CardSystem/index.html', params)


# 登录页面 [基本OK]
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # 检测username的字符组成
        check = check_name.match(username)
        if check:
            is_matched = models.Users.objects.filter(username=username, password=password)  # 查找输入是否匹配
            if is_matched:
                request.session['login_user'] = username                # 登陆成功记录session信息
                request.session['message'] = 'welcome, ' + username     # 返回登陆成功信息
                return HttpResponseRedirect('/index')
            else:
                return render(request, 'CardSystem/login.html', {'error2': '用户名不存在或者密码错误!'})
        else:
            return render(request, 'CardSystem/login.html', {'error1': '用户名只能由数字和字母组成!'})
    else:
        message = request.session.get('message', '')    # 显示注册成功信息
        if message != '':
            del request.session['message']
            return render(request, 'CardSystem/login.html', {'message': message})
        return render(request, 'CardSystem/login.html')


# 注册页面 [基本OK]
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        # 检测用户名输入的合法性 [缺少长度和字符组成判断]
        check = check_name.match(username)                              # 用户名只能有字符和数字组成, 长度为6-18
        if check:
            is_exist = models.Users.objects.filter(username=username)   # 判断用户名是否已经存在
            if is_exist:
                return render(request, 'CardSystem/register.html', {'error1': '用户名已经存在!'})
            else:
                check2 = check_pass.match(password)                     # 密码长度为8-18
                if check2:
                    if password != password2:                           # 判断两次输入的密码是否一致
                        return render(request, 'CardSystem/register.html', {'error3': '两次密码输入不一致!'})
                    else:                                               # 输入合法, 将数据插入数据表
                        models.Users.objects.create(username=username, password=password)
                        request.session['message'] = '注册成功!'
                        return HttpResponseRedirect('/card/login')
                else:
                    return render(request, 'CardSystem/register.html', {'error2': '密码长度为8-18位!'})
        else:                                                           # 用户名出现数字和字母以外的字符
            return render(request, 'CardSystem/register.html', {'error1': '用户名只能由数字和字母组成, 长度为6-18位!'})
    else:
        return render(request, 'CardSystem/register.html')



# 名片页面
def card(request):
    pass

#创建个人页面
@csrf_exempt
def edit(request):
    if request.method == 'GET':
        return render(request, 'CardSystem/edit.html')
    elif request.method == 'POST':
        username = request.session.get('login_user', "")
        title = request.POST['title']
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        wechat = request.POST['wechat']
        qq = request.POST['qq']
        is_exist = models.Cards.objects.filter(username=username, title=title, name=name, phone=phone, address=address, email=email,
                                               wechat=wechat, qq=qq)
        if is_exist:
            return HttpResponse("已经存在了")
        else:
            models.Cards(username=username, title=title, name=name, phone=phone, address=address, email=email, wechat=wechat, qq=qq).save()
            return HttpResponse("创建成功！")

@csrf_exempt
def messages(request):
    if request.method == 'GET':
        return render(request, 'CardSystem/messages.html')

