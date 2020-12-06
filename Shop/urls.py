from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name ='home'),
    path('update_item/', views.updateItem, name='update_item'),
]
urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)