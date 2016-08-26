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
    url(r'^answer/$', answer, name='answer'),
    url(r'^compare/(?P<secret1>\d+)/(?P<secret2>\d+)/$', compare, name='compare'),
)
