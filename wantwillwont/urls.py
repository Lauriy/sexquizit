from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from wantwillwont.apps.wantwillwont_web.views import HomeView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^$', HomeView.as_view(), name='home'),
)
