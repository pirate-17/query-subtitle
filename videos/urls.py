from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.upload_file, name="home"),
    path("search_keywords", views.search_keyword, name="search-keywords"),
]
