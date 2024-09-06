
from django.urls import path 
from . import views

urlpatterns = [    
    path('test1', views.test1),
    path('test2', views.test2),
    path('test3', views.test3),
    path('test4', views.test4),
    path('test5', views.test5),
    path('test6', views.test6),
]
