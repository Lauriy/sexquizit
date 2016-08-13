# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.translation import activate


class TestHomePage(TestCase):
    def test_uses_base_template(self):
        activate('en')
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'base.html')
