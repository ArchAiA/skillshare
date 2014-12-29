from django.conf.urls import patterns, include, url

from django.conf import settings #! import settings
from django.conf.urls.static import static #! import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mvp_landing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'signups.views.home', name='home'),
    url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'), # This creates an entry stating that [#/thank-you] should be rendered by the thankyou class defined in views.py
    url(r'^about-us/$', 'signups.views.aboutus', name='aboutus'),
)

if settings.DEBUG: #! If you are in DEBUG mode, then append the below to the urlpatterns variable
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)