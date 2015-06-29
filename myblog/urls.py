from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^', 'blog.views.index', name="index"),
    url(r'^', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
