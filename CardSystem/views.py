from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from CardSystem import models
from django.views.decorators.csrf import csrf_exempt

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