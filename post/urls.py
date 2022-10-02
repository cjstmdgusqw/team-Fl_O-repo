from django.urls import path, include
from . import views

urlpatterns = [
    path('post/', include("post.urls")),
    path('posting/', views.posting),
]