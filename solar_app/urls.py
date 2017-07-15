from django.conf.urls import url

from .views import *

urlpatterns = [    
    url(r'summary-average', SiteSummaryAverage.as_view(), name='site-summary-average'),
    url(r'summary', SiteSummary.as_view(), name='site-summary'),    
    url(r'sites/(?P<pk>[0-9]+)$', SiteDetail.as_view(), name='site-detail'),
    url(r'sites', SiteList.as_view(), name='site-list'),
    url(r'', SiteList.as_view(), name='site-list-default')
]