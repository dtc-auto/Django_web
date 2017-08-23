from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # index page
    url(r'^$', 'autohome_pages.views.base', name='index'),
    # dashboard page
    url(r'^dashboard$', 'autohome_pages.views.dashboard', name='dashboard'),
    # charts and pages with chart
    url(r'^level1$', 'autohome_pages.views.level1chart', name='level1'),
    url(r'^level1Page$', 'autohome_pages.views.level1ChartPage', name='level1Page'),
    url(r'^level2$', 'autohome_pages.views.level2chart', name='level2'),
    url(r'^level2Page$', 'autohome_pages.views.level2ChartPage', name='level2Page'),
    url(r'^region/$', 'autohome_pages.views.carOwnerChart', name='region'),
    url(r'^regionPage/$', 'autohome_pages.views.carOwnerChartPage', name='regionPage'),
    url(r'^purpose/$', 'autohome_pages.views.purposeChart', name='purpose'),
    url(r'^purposePage/$', 'autohome_pages.views.purposeChartPage', name='purposePage'),
    # admin page
    url(r'^admin/', include(admin.site.urls)),
)
