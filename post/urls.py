from django.urls import path 
from .views import getAllArticles, getArticle, createarticle

urlpatterns = [
    path("getarticles/", getAllArticles),
    path('getarticle/<int:id>', getArticle),
    path("createarticle/", createarticle)
]