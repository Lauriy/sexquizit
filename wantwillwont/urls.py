from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from wantwillwont.views import HomeView, home_files

urlpatterns = [
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$', home_files, name='home_files'),
]

urlpatterns += i18n_patterns(
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += [
        url(r'^rosetta/', include('rosetta.urls')),
    ]
