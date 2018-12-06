from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',
                           'home.views.supno',
                           name='supno'),

                       url(r'^supno$',
                           'home.views.supno',
                           name='supno'),

                       url(r'^year$',
                           'home.views.year',
                           name='year'),

                       url(r'^name$',
                           'home.views.name',
                           name='name'),

                       url(r'^all$',
                           'home.views.all',
                           name='all'),

                       url(r'^year-2015$',
                           'home.views.bes',
                           name='bes'),

                       url(r'^year-2016$',
                           'home.views.alti',
                           name='alti'),

                       url(r'^year-2017$',
                           'home.views.yedi',
                           name='yedi'),

                       url(r'^year-2018$',
                           'home.views.sekiz',
                           name='sekiz'),

                       url(r'^all-extended$',
                           'home.views.detayli',
                           name='detayli'),

                       )

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$',
                             'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

if settings.DEBUG:   # if DEBUG is True it will be served automatically
    urlpatterns += patterns('',
                            url(r'^static/(?P<path>.*)$',
                                'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                            )