from django.conf.urls import include, url
from django.contrib import admin

from wantwillwont.views import HomeView, home_files

urlpatterns = [
    url(r'^', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$', home_files, name='home-files'),
]
