# hub/urls.py
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_superuser/', views.create_superuser, name='create_superuser'),
    path('search/', views.search, name='search'),

    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/create/', views.project_create, name='create_project'),
    path('project/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('project/<int:pk>/delete/', views.delete_project, name='delete_project'),

    
    path('forum/', views.forum_post_list, name='forum_post_list'),
    path('forum/<int:post_id>/', views.forum_post_detail, name='forum_post_detail'),
    path('forum/create/', views.create_forum_post, name='create_forum_post'),
    path('forum/create-category/', views.create_category, name='create_category'),
    path('forum/post/<int:post_id>/edit/', views.edit_forum_post, name='edit_forum_post'),
    path('forum/post/<int:post_id>/delete/', views.delete_forum_post, name='delete_forum_post'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),


    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
