# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse

from datetime import date

from .models import *


def create_base_case():
        site_a = SiteModel.objects.create(name='SiteA')
        site_b = SiteModel.objects.create(name='SiteB')

        SiteDetailModel.objects.create(site=site_a, val_a=10, val_b=20, date=date.today())
        SiteDetailModel.objects.create(site=site_a, val_a=20, val_b=30, date=date.today())


class SiteModelTests(TestCase):

    def test_list_all_site_model(self):
        """
        Test all site
        """
        create_base_case()

        self.assertIs(SiteModel.objects.all().count(), 2)


class SiteDetailModelTests(TestCase):

    def test_avg_by_each_site(self):

        create_base_case()

        obj_avg = SiteDetailModel.objects.get_average_by_each_site()[0]

        self.assertEqual(obj_avg['site_name'], u'SiteA')
        self.assertEqual(obj_avg['val_a'], 15)
        self.assertEqual(obj_avg['val_b'], 25)
    
    def test_sum_by_each_site(self):

        create_base_case()

        obj_avg = SiteDetailModel.objects.get_sum_by_each_site()[0]

        self.assertEqual(obj_avg['site_name'], u'SiteA')
        self.assertEqual(obj_avg['val_a'], 30)
        self.assertEqual(obj_avg['val_b'], 50)
        


class SiteListViewTests(TestCase):

    def test_site_list_view(self):

        create_base_case()

        response = self.client.get(reverse('site-list-default'))

        self.assertEqual(response.status_code, 200)        
        self.assertEqual(len(response.context['object_list']), 2)


class SiteDetailViewTests(TestCase):

    def test_site_detail_view(self):

        create_base_case()

        site_a = SiteModel.objects.get(name='SiteA')

        response = self.client.get(reverse('site-detail', args=(site_a.pk,)))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, site_a.name)        