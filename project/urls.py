from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<str:pk>', views.details, name='details'),
    path('send_mail', views.contact_me, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)