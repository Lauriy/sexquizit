from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from want_will_wont.apps.want_will_wont_web.views import HomeView, start_answering, resume_answering

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^answer/$', start_answering, name='answer_set_start'),
    url(r'^answer/(?P<pk>\d+)/$', resume_answering, name='answer_set_resume'),
)