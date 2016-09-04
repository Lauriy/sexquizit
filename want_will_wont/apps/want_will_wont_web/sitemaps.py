from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class StaticViewSitemap(Sitemap):
    priority = 1
    changefreq = 'daily'

    def items(self):
        return ['home', 'about', 'answer_male', 'answer_female', 'compare']

    def location(self, item):
        return reverse(item)
