from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='articles'),
    path('post/<int:article_id>', views.detail, name='detail')
]