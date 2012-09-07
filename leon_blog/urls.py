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

    # about
    url(r'^about/$', 'blog.views.about'),
)
