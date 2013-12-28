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
    url(r'^contact/$', 'daddy_app.views.contact'), # contact form
    url(r'^thanks/$', 'daddy_app.views.login_view'), # thanks page after contacting
    url(r'^map/$', 'daddy_app.views.show_map'), # map page
    url(r'^mappoi/$', 'daddy_app.views.show_mappoi'), # map poi page
    url(r'^users/$', 'daddy_app.views.users'),
    url(r'^users/(?P<username>\w{0,30})/$', 'daddy_app.views.users'),
    url(r'^follow$', 'daddy_app.views.follow'),
    # all auth urls:
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
