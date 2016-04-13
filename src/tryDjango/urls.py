from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'profiles.views.index', name='index'),
    url(r'^about/$', 'profiles.views.about', name='about'),
    url(r'^profile/$', 'profiles.views.profile', name='profile'),
    url(r'^contact/$', 'contact.views.contact', name='contact'),
    url(r'^checkout/$', 'checkout.views.checkout', name='checkout'),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, documents_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)