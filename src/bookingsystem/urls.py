from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^view/', 'home.views.view'),
    url(r'^cancel/', 'home.views.cancel'),
    url(r'^book/', 'home.views.book'),
    url(r'^admin/', include(admin.site.urls)),
)
