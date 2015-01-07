#encoding=utf8

from django.conf.urls import patterns, include, url
from django.contrib import admin

#from Demo import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoDJ.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^demo/', include('Demo.urls')),
)
