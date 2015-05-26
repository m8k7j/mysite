#-*-coding:utf-8-*-
from django.conf.urls import patterns, include, url
from sblog import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
	url(r'^bloglist/$',views.blog_list),
	url(r'^blog/(\d+)/$',views.blog_show),
	url(r'^tag/(\d+)/$',views.blog_filter),
	url(r'^add_blog/$',views.blog_add),
	url(r'^update_blog/$',views.blog_update),
	url(r'^blog/(\d+)/del/$',views.blog_delete),

	
	

)
