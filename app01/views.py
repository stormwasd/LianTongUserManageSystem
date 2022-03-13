from django.shortcuts import render, HttpResponse

# Create your views here.


def UserList(request):
    # return HttpResponse('欢迎使用')
    return render(request, 'UserList.html')


def tpl(request):
    name = '韩超'
    roles = ['管理员', 'CEO', '保安']
    user_info = {'name': '郭智', 'salary': '100000', 'role': 'CTO'}
    data_list = [
        {'name': '郭1', 'salary': '100000', 'role': 'CTO'},
        {'name': '郭2', 'salary': '100000', 'role': 'CTO'},
        {'name': '郭3', 'salary': '100000', 'role': 'CTO'}
    ]
    return render(request, 'tpl.html', {"n1": name, "n2": roles, "n3": user_info, "n4": data_list})


def news(request):
    return render(request, 'news.html')