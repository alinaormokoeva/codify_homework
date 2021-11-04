from  django.urls import path
from . import views

urlpatterns =[
    path('create/', views.create, name='create_article'),
    path('articles/', views.article_list, name='articles')
]