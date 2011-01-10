### -*- coding: utf-8 -*- ####################################################

from django.http import HttpResponse

from .models import set_group 

def remember_group(request, group):
    set_group(request, request.REQUEST.get(group))
    return HttpResponse('1', content_type="text/plain; charset=utf-8")
