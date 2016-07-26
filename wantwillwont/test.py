# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase


class TestHomePage(TestCase):
    def test_uses_base_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'base.html')
