### -*- coding: utf-8 -*- ####################################################

PARAM_NAME = 'firstletter'

def term_lookup(request, param_name=PARAM_NAME):
    return request.REQUEST.get(param_name, '')

def alphabetic_setup(request, object_list, field_name='title', param_name=PARAM_NAME):
    term = term_lookup(request, param_name)
    if term:
        if hasattr(object_list, 'filter'):
            object_list = object_list.filter(**{"%s__iregex" % field_name: r'^[%s]' % term})
        else:
            object_list = filter(lambda obj: getattr(obj, field_name).startswith(term), object_list)
    
    return object_list
