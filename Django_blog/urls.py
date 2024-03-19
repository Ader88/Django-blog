from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/<int:pk>/', views.post_details, name='post_details'),
    path('posts/add/', views.add_post, name='add_post'),
    path('authors/', views.authors_list, name='authors_list'),
    path('authors/<int:pk>/', views.author_details, name='author_details'),
    path('authors/add/', views.add_author, name='add_author'),
]