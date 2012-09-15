from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # blog
    url(r'^blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[-\w]+)/$', \
        'blog.views.post', name='leon_blog'),
    url(r'^blogs/$', 'blog.views.blogs'),

    # home
    url(r'^$', 'blog.views.index'),

    # category
    url(r'^category/(?P<slug>[-\w]+)/$', 'blog.views.category'),

    # archive
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', 'blog.views.archive'),

    # tag
    url(r'^tag/(?P<tag>[-\w]+)/$', 'blog.views.tags'),

    # about
    url(r'^about/$', 'blog.views.about'),

    # comments
    url(r'^comments/', include('django.contrib.comments.urls')),
)
