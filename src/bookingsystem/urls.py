from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'home.views.home', name='home'),
    url(r'^view/', 'home.views.view', name='view'),
    url(r'^cancel/', 'home.views.cancel', name='cancel'),
    url(r'^book/', 'home.views.book', name='book'),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', 'home.views.logout_view'),
)
