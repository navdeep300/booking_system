from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login,logout

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^view/', 'home.views.view', name='view'),
    url(r'^cancel/', 'home.views.cancel', name='cancel'),
    url(r'^book/', 'home.views.book', name='book'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
)
