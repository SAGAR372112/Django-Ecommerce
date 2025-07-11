from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('securitypanel/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('orders/', include('orders.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
