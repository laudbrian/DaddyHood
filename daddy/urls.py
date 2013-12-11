from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'daddy_app.views.index'), # root
    url(r'^login$', 'daddy_app.views.login_view'), # login
    url(r'^logout$', 'daddy_app.views.logout_view'), # logout
    url(r'^signup$', 'daddy_app.views.signup'), # signup
    url(r'^notes$', 'daddy_app.views.public'), # public notes
    url(r'^submit$', 'daddy_app.views.submit'), # submit new note
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
