# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from django.db.models import Count, Sum, Avg
from django.db.models.functions import Coalesce


class SiteModel(models.Model):

    name = models.CharField(max_length=255)    

    def get_absolute_url(self):
        return reverse('site-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class SiteDetailManager(models.Manager):

    def get_by_site_pk(self, site_pk):
        return super(SiteDetailManager, self).get_queryset().all()\
                    .filter(site__pk=site_pk).order_by('date')
    
    def get_average_by_each_site(self):
        return super(SiteDetailManager, self).get_queryset().all()\
                    .values('site')\
                    .annotate(site_name=Coalesce('site__name', 'site')\
                              ,site_count=Count('site'), val_a=Avg('val_a'), val_b=Avg('val_b'))\
                    .order_by('site')
    
    def get_sum_by_each_site(self):
        obj_all = super(SiteDetailManager, self).get_queryset().all()
        
        group_dict = {}
        
        for site_detail in obj_all:

            _pk = site_detail.site.pk

            if _pk in group_dict:
                obj = group_dict[_pk]
                obj['val_a'] += site_detail.val_a
                obj['val_b'] += site_detail.val_b                
            else:
                group_dict[_pk] = {
                    'site_name': site_detail.site.name,
                    'val_a': site_detail.val_a,
                    'val_b': site_detail.val_b
                }
        
        return group_dict.values()


class SiteDetailModel(models.Model):

    site = models.ForeignKey(SiteModel, on_delete=models.CASCADE)
    val_a = models.FloatField()
    val_b = models.FloatField()
    date = models.DateTimeField()

    objects = SiteDetailManager()

    def __str__(self):
        return "{0} - {1}|{2}".format(self.site.name, self.val_a, self.val_b)