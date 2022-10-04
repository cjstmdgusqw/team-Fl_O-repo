from django.urls import path, include
from . import views
from django.urls import path
from .views import Main, UploadFeed
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', Main.as_view()),
    path('posting/', views.posting),
    path('comment/', views.comment),
] 
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)