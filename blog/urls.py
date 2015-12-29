from django.conf.urls import url

urlpatterns = [
	url(r'^$', 'blog.views.index', name="index"),
	# url(r'^post/(?P<pk>\d+)/$', 'blog.views.post', name='post'),
	url(r'^post/(?P<pk>\d+)/$', "blog.views.post", name="post"),
	url(r'^category/(?P<pk>\d+)/$', "blog.views.category", name="category"),
	url(r'^about$', 'blog.views.about', name="about"),
	url(r'^create/$', 'blog.views.create', name="create"),
	url(r'^post/(?P<pk>\d+)/edit$', "blog.views.edit", name="edit"),

]

