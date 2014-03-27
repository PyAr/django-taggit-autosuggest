try:
    # Django < 1.6
    from django.conf.urls.defaults import *
except ImportError:
    # Django >= 1.6
    from django.conf.urls import patterns, url


urlpatterns = patterns('taggit_autosuggest.views',
    url(r'^list/$', 'list_tags', name='taggit_autosuggest-list'),
)
