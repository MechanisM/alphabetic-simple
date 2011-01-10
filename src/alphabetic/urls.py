### -*- coding: utf-8 -*- ####################################################

from django.conf.urls.defaults import *


urlpatterns = patterns('alphabetic.views',
    url('^remember_group/(?P<group>[-\w]+)/', 'remember_group', name="remember_group"),
)
