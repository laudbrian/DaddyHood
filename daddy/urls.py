from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'daddy_app.views.index'), # root
    url(r'^login$', 'daddy_app.views.login_view'), # login
    url(r'^logout$', 'daddy_app.views.logout_view'), # logout
    url(r'^signup$', 'daddy_app.views.signup'), # signup

    url(r'^admin/', include(admin.site.urls)),
)
