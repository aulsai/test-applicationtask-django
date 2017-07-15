# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import *


class SiteList(ListView):
    template_name = 'solar_app/site_list.html'    
    model = SiteModel
    

class SiteDetail(ListView):
    template_name = 'solar_app/site_detail.html'
    
    def get_queryset(self, param=None):        
        site_pk = self.kwargs['pk']        
        return SiteDetailModel.objects.get_by_site_pk(site_pk)

    def get_context_data(self, **kwargs):
        context = super(SiteDetail, self).get_context_data(**kwargs)

        # Get SiteName
        site_pk = self.kwargs['pk']
        site_name = SiteModel.objects.get(pk=site_pk)

        context.update({
            'object': site_name
        })        

        return context


class SiteSummary(TemplateView):
    template_name = 'solar_app/site_summary.html'

    def get_context_data(self, **kwargs):
        context = super(SiteSummary, self).get_context_data(**kwargs)

        context.update({            
            'object_list': SiteDetailModel.objects.get_sum_by_each_site()
        })

        return context


class SiteSummaryAverage(ListView):
    template_name = 'solar_app/site_summary.html'

    def get_queryset(self):
        return SiteDetailModel.objects.get_average_by_each_site()