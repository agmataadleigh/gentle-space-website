
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This points the root URL to your homepage app
    path('', include('homepage.urls')), 
]
