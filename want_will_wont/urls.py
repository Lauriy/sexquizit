from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from want_will_wont.apps.want_will_wont_web.views import home, answer, compare, about

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^answer/(?P<gender>male|female)/$', answer, name='answer'),
    url(r'^answer/(?P<gender>male|female)/(?P<secret2>[\w-]+)/$', answer, name='answer_response'),
    url(r'^compare$', compare, name='compare'),
    url(r'^compare/(?P<secret1>[\w-]+)$', compare, name='compare'),
    url(r'^compare/(?P<secret1>[\w-]+)/(?P<secret2>[\w-]+)/$', compare, name='compare'),
)
