from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path('detail/<int:question_id>', views.detailView, name='detail'),
    path('<int:question_id>', views.vote, name='vote'),
    path('list/', views.viewlist, name='viewlist'),
    path('', views.index, name='index'),
]
