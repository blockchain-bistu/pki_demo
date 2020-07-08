#！/usr/bin/env python
# _*_ coding:utf-8 _*_

from django.http import HttpResponseRedirect

def check_login(fn):
    def wrapper(request,*args,**kwargs):
        if request.session.get('IS_LOGIN', False):
            return fn(request,*args,*kwargs)
        else:
            # 获取用户当前访问的url，并传递给/pki/denglu/
            next = request.get_full_path()
            red = HttpResponseRedirect('/pki/denglu/?next=' + next)
            return red
    return wrapper