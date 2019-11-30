# encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from ksglapp.models import Stinfo,OpenDoor,AppleLog
from django.http.response import JsonResponse
from ksglapp.getkey import get_key as gy
import templates

import time

key_ = "001100"    # 初始秘钥
def confirm(request):
    global key_
    if request:
        xh = request.GET['number']
        pd = request.GET['password']
        phone = request.GET['phone']
        print('{1}\n|{0: ^22}|\n{1} '.format('蜜罐管理','-'*28))
        print('| {0:<25}| \n| 学号：{1: <19}| \n| 密码：{2: <19}| \n| 手机号：{3: <17}| \n{4}'.format(time.strftime('%m-%d: %H:%M:%S'),xh,pd,phone,'-'*28))
        
        try:
            xh = str(eval(xh))
            db_data = Stinfo.objects.get(st_id = xh)
            qx = OpenDoor.objects.get(fsid = xh)

			# 密码判断
            if db_data.st_password == pd:
            	# 权限判断
            	if qx.spermissions == True:
            		data = key_
            		# 添加日志
            		rz = AppleLog()
            		rz.stime = time.strftime("%m-%d %H:%M:%S", time.localtime())
            		rz.sid = xh
            		rz.sprofessional = db_data.st_major
            		rz.sphone = phone
            		rz.sresults = 1
            		rz.save()
            	else:
            		data = '权限不足，请联系管理员'

            print('| 确认颁发秘钥：{0}     |\n{1}'.format(data,'-'*28))

        except:
            print('|{0: ^22}| \n{1}'.format('申请失败','-'*28))

            data = '请检查账户或者密码'
        else:
            pass
        
        
    data_json = {
        'key':data
    }
    return JsonResponse(data_json, safe=False)
def update_key(request):
    global key_
    key_ = gy()
    return JsonResponse(key_, safe=False)

def index(request):
    return render(request, 'zy/index.html')
#     return HttpResponse('<h1>test</h1>')
