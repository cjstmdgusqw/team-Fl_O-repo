from django.urls import path
from . import views

urlpatterns =[
     path('', views.main),
     path('signup/', views.signup),
     path('index/', views.index),
     path('profile/', views.profile),
    
]