from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('nstapi', views.nstapi, name='nstapi'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('delete_comment/<int:article_pk>/<int:comment_pk>', views.delete_comment, name='delete_comment'),

]