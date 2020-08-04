from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from. import views

urlpatterns = [
    path('', views.home, name='home-home'),
    path('about/', views.about, name='home-about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

