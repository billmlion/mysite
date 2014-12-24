from django.conf.urls import patterns, include, url
from django.contrib import admin
from books import views
from django.contrib import auth
from mysite.views import hello
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    #use for login and logout 
    (r'^accounts/login/$',login),
    (r'^accounts/logout/$',logout),
    (r'^logout/$',views.logout_view),
    #('^hello/$', hello),
    (r'^search-form/$', views.search_form),
    (r'^search/$',views.search),
    (r'^contact/$',views.contact),
    (r'^books/$',views.getBooks),
    #use for user register
    (r'^register/$',views.register),

    
)
