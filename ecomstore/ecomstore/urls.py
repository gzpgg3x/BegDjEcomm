from django.conf.urls import *
from ch2.models import *
from ch2.views import catalog

from ecomstore import settings 

# from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'ecomstore.views.home', name='home'),
#     # url(r'^ecomstore/', include('ecomstore.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),

#     (r'^catalog/$', 'ch2.views.catalog'), 
# )

# urlpatterns += patterns('', 
urlpatterns = patterns('', 
    #other commented code here 
    # (r'^catalog/$', 'ch2.views.home'),
    (r'^catalog/?', 'ch2.views.home'), 
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : 'C:/Users/fpan/PY-Programs/BegDjEComm/ecomstore/ecomstore/static/' }),     
)