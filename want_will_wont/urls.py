from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings

from want_will_wont.apps.want_will_wont_web.views import home, answer, compare, about, contact

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^answer/(?P<gender>male|female)/$', answer, name='answer'),
    url(r'^answer/(?P<gender>male|female)/(?P<secret2>[\w-]+)/$', answer, name='answer_response'),
    url(r'^compare/$', compare, name='compare'),
    url(r'^compare/(?P<pk1>\d+)/$', compare, name='compare_1'),
    url(r'^compare/(?P<pk1>\d+)/(?P<pk2>\d+)/$', compare, name='compare_1_2'),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', url(r'^rosetta/', include('rosetta.urls')), )
