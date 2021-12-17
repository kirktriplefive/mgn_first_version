from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('post/<slug:slug>/edit/',views.BlogUpdateView.as_view(), name='post_edit'),
    path("main/", views.Posts.as_view(), name= "posts"),
    path("main/search", views.PostsSearch.as_view(), name= "posts_search"),
    path("main/sort/", views.sort, name= "posts_sort"),
    path("main/sort_date/", views.sort_date, name= "posts_sort_by_date"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="view_post"),  
    path('post/new/', views.post_new, name="post_new"),
    path("comment/<int:pk>/", views.AddComment.as_view(), name="add_comment"),


    
]
