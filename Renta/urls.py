from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('catalogo.urls')),
    path('', RedirectView.as_view(url='/home/', permanent=True)),
]
#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('cuentas/', include('django.contrib.auth.urls')),
]


# Use static() to add url mapping to serve static files during development (only)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)