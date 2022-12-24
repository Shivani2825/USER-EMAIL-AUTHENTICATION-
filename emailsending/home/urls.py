from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('sendemail', views.sendmail),
    path('login',views.login)
]
