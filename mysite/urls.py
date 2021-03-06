from django.conf.urls import patterns, include, url
from django.contrib import admin
from books import views
from django.contrib import auth
from mysite.views import hello
from django.contrib.auth.views import login, logout
admin.autodiscover()

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
    (r'^login_view/$',views.login_view),#custom login process
    #('^hello/$', hello),
    (r'^search-form/$', views.search_form),
    (r'^search/$',views.search),
    (r'^contact/$',views.contact),
    url(r'^books/$',views.getBooks),

    url(r'^updateBook/(\d+)/$',views.updateBook,name='updateBook'),
    (r'^getBookById/(\d+)/$', views.getBookById),

    #use for user register
    (r'^register/$',views.register),
    url(r'^getArticle/$',views.getArticle),
    url(r'^updateArticle/(\d+)/$',views.updateArticle,name='updateArticle'),
    
)
