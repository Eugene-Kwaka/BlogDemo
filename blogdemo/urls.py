from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# Sitemaps configuration
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from blogdemo.sitemaps import CategorySitemap, PostSitemap

sitemaps = {'category':CategorySitemap, 'post': PostSitemap}

# robots_txt 
from core.views import robots_txt

urlpatterns = [
    # the sitemaps url path
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    # robots_txt 
    path('robots_txt', robots_txt, name='robots_txt'),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('blog.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
