from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('category/<int:id>/', views.article_by_category, name='article_by_category'),
    path('contact/',views.contact,name='contact'),
]
