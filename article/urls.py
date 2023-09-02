from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.ArticleList.as_view()),
    path('create/', views.ArticleCreate.as_view()),
    path('<int:pk>/', views.ArticleDetail.as_view()),
    path('update/<int:pk>/', views.ArticleUpdate.as_view()),
    path('delete/<int:pk>/', views.ArticleDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
