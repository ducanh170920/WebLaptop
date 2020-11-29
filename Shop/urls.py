from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name ='home'),

]
urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)