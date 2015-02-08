from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bookingsystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^view/', 'bookingsystem.views.view'),
    url(r'^cancel/', 'bookingsystem.views.cancel'),
    url(r'^book/', 'bookingsystem.views.book'),
    url(r'^admin/', include(admin.site.urls)),
)
