from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
]
