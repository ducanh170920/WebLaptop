from django.urls import path
from . import views
app_name = 'news'
urlpatterns = [
    path("register/", views.register, name="register"),
    path('process/', views.process, name='pro'),
    path('email/', views.email_view, name='email'),
    path('save/', views.save_news, name='save'),
    path('add/', views.add_post, name='add'),
    path('', views.index, name="index"),
]
