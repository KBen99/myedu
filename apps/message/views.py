from django.shortcuts import render
from .models import UserMessage
def index(request):
#一、将数据存入数据库 了解：django/db/models/base.py 源码中提供save方法
    # 存储部分
    # 首先实例化一个对象
    user_message = UserMessage()
    # 为对象增加属性
    user_message.name = "mtianyan2"
    user_message.message = "blog.mtianyan.cn"
    user_message.address = "西安"
    user_message.email = "1147727180@qq.com"
    user_message.object_id = "efgh"
    # 调用save方法进行保存
    user_message.save()

#二、如何从html的提交中取到数据并保存进数据库
    #数据库新增
    # 此处对应html中的method="post"，表示我们只处理post请求
    if request.method== 'POST':
        # 就是取字典里key对应value值而已。取name，取不到默认空
        name=request.POST.get('name','')
        message=request.POST.get('message','')
        address=request.POST.get('address','')
        email=request.POST.get('email','')
        # 实例化对象
        user_message = UserMessage()
        # 将html的值传入我们实例化的对象.
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        # 调用save方法进行保存
        user_message.save()

#三、删除数据 对于查询到的数据做删除：
    # 方法2 :filter取出指定条件值，逗号代表and 必须同时满足两个条件才返回。
    all_message = UserMessage.objects.filter(name='mtianyan2', address='西安')
    # 我的数据库里保存着可以匹配到该条数据的一行。
    # 删除操作：使用delete方法删除all_message
    all_message.delete()

    for message in all_message:
        # 删除取到的message对象
        message.detele()
        # print message.name
    return render(request,'message_form.html')

# Create your views here.
