
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('imageseg/',views.image_seg,name='image_seg'),
    path('thug/',views.thug,name='thug'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)