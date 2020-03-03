from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('webapp/',include('webapp.urls')),
    path('it/',include('inteligence.urls')),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
